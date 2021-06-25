import  torch.nn as nn

class SwinTrasnformer(nn.Module):
    def __init__(self,hidden_dim, layers, heads, channels=3, num_classes=1000,head_dim=32,
                      window_size=7,downscaliing_factors=(4,2,2,2),relative_pos_embedding=True):
        super(SwinTrasnformer, self).__init__()
        self.stage1=StageModule(incha)

    def forward(self):

        return 1