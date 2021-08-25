from PIL import Image, ImageChops
import requests as rq


def download_image(url: str):
    res = rq.get(url, stream=True)
    data = b''
    for chunk in res.iter_content(chunk_size=88):
        if(chunk):
            data += chunk
    with open('./img-net/lena.png', 'wb') as f:
        f.write(data)


def main():
    url = 'https://cdn.goskills.com/blobs/blogs/409/e7133082-497d-4557-b52b-56794a94e06f.png'

    download_image(url)

    with Image.open('./img-net/lena.png', 'r') as img:
        inv = ImageChops.invert(img)
        inv.save('./img-net/lena-inverted.png')


if __name__ == '__main__':
    main()
