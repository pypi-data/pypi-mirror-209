from setuptools import setup, find_packages

setup (
  name='jdclip',
  version='0.0.2',
  description='A demo of model',
  url='',  
  author='jaideep ',
  author_email='jaideepkaushal2@gmail.com',
  license='MIT', 
  keywords='image search', 
  packages=find_packages(),
  install_requires=['torch','Pillow','openai-clip','torchvision'],
  dependency_links=[
        #"https://openaipublic.azureedge.net/clip/models/40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af/ViT-B-32.pt"
        "https://openaipublic.azureedge.net/clip/models/7e526bd135e493cef0776de27d5f42653e6b4c8bf9e0f653bb11773263205fdd/RN50x4.pt"
    ]
)