import clip
import os
import torch
import PIL.Image as Image
device ="cpu"
model, preprocess = clip.load('ViT-L/14', device)
img_featureslist=[]
def read_folder(path):
    pair_dir={}
    result=[]
    for roots, dirs, files in os.walk(path):
          for dirs in files:
                result.append(os.path.join(roots, dirs))
    for j,i in enumerate(result):
                    pair_dir[j] = i
    return pair_dir
def image_feature_extract(path):
        image = Image.open(path)
        image_input = preprocess(image).unsqueeze(0).to(device)
        with torch.no_grad():
            image_features = model.encode_image(image_input)
        return image_features
def extract_textfeatures(txt_input):
    search = txt_input
    text_inputs = clip.tokenize(search).to(device)
    text_features = model.encode_text(text_inputs)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    return text_features
def get_imagefeatures(path,pair_dir):
    #result = get_image_path(path)
    for i in range(0,len(pair_dir)):
        img_featureslist.append(image_feature_extract(pair_dir[i]))
def similar_F(path,txt):
    result_dir={}
    end_result=[]
    pair_dir={}
    txt_len = len(txt.split())
    if(txt_len<3):
        threshold=34-(1*txt_len)
    else:
        threshold =30+(1*txt_len) 
    text_answer = extract_textfeatures(txt)
    pair_dir = read_folder(path)
    if(len(img_featureslist) == 0):
            get_imagefeatures(path,pair_dir)
    with torch.no_grad():
        for k in range(0, len(img_featureslist)):
            ans = (10* img_featureslist[k] @ text_answer[0])
            if(ans>threshold):
                result_dir[k]=ans
        result_dir = dict(sorted(result_dir.items(), key=lambda item: item[1],reverse =True))
        #print(result_dir)
        for i in result_dir:
            if i in pair_dir:
                j = pair_dir[i]
                end_result.append(j)
    return(end_result)
