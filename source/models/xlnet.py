from pytorch_transformers import XLNetModel, XLNetConfig
import torch
from torch import nn
from models.token_layers import TokenClsLayer, SentClsLayer


class XLNetForWSD(nn.Module):
    """     
    Base XLNet model with a token selection layer and a binary classifier layer
    for model_type refer to https://github.com/huggingface/pytorch-transformers  
    
    for the token_layer token layer parameter there are three possible choices:
    
    'token-cls'
    'sent-cls'
    'Sent-cls-ws' 

    this is inspired from https://arxiv.org/pdf/1908.07245.pdf
    
    
    """ 
  
    def __init__(self, num_labels=2, model_type='xlnet-base-cased',token_layer='token-cls',output_logits=True):
        super(XLNetForWSD, self).__init__()
        
        self.config = XLNetConfig()
        self.token_layer = token_layer
        self.num_labels = 2
        self.xlnet = XLNetModel.from_pretrained(model_type)
        self.dropout = nn.Dropout(self.config.hidden_dropout_prob)
        self.output_logits = output_logits
        
        # Define which token selection layer to use
        if token_layer == 'token-cls':
            self.tokenselectlayer = TokenClsLayer()
        elif token_layer in ['sent-cls','sent-cls-ws']:
            self.tokenselectlayer = SentClsLayer()
        else:
            raise ValueError("Unidentified parameter for token selection layer")       
                 
        self.classifier = nn.Linear(768, num_labels)
        if not output_logits:
            self.softmax = nn.Softmax(dim=1) # to be checked!!!
        
        nn.init.xavier_normal_(self.classifier.weight)   
    
    def forward(self, _tokens_tensor, _sentence_tensor, _target_token_ids):
        
        _encoded_layers, _ = self.xlnet(_tokens_tensor, _sentence_tensor)
        #print(_encoded_layers)
        # One token selection layer takes 2 imputs otherwise takes only one
        
               
        if self.token_layer == 'token-cls':
            #ipdb.set_trace()
            _target_token_embeddings = self.tokenselectlayer(_encoded_layers,_target_token_ids)
        else:
            _target_token_embeddings = self.tokenselectlayer(_encoded_layers)
        pooled_output = self.dropout(_target_token_embeddings)
        logits = self.classifier(pooled_output)
        if self.output_logits:
            return logits
        return self.softmax(logits)