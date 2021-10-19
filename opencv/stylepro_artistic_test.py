import cv2
import paddlehub as hub

if __name__ == '__main__':
    stylepro_artistic = hub.Module(name="stylepro_artistic")
    result = stylepro_artistic.style_transfer(
        images=[{
            'content': cv2.imread('imges/aes.jpg'),
            'styles': [cv2.imread('imges/img.png')]
        }], use_gpu=True,visualization=True)
