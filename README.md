# {Title}

{Logo}

{
    생성을 하고 싶은 이미지와 비슷한 Reference 이미지를 사용하여 새로운 이미지 생성에 필요로 하는 알맞은 Postive tag와 Negative tag를 추출합니다. 이를 통해 최소한의 시도로 원하는 이미지를 획득할 수 있도록 도움을 주는 소프트웨어입니다.
}

# Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Support and Feeback](#support-and-feedback)
5. [About Easy Diffuser](#about-easy-diffuser)
6. [Licenses](#licensed)

---

## Features

{
 * run_link: 이미지 링크를 삽입하면 해당 이미지와 관련된 Positive prompt와 Negative prompt를 생성합니다.
 * run_image: 이미지 파일을 삽입하면 해당 이미지와 관련된 Positive prompt와 Negative prompt를 생성합니다. 
 * print_caption: run_link 또는 run_image를 통해 생성된 태그들을 출력합니다.
 * send2ui: 생성된 태그들을 WEBUI로 전송합니다. Stable Diffusion이 해당 태그들을 받아 태그와 관련된 이미지를 생성하여 로컬 저장소에 저장합니다. 
 * input_link: 이미지 링크를 삽입하면 모델이 학습할 수 있는 이미지 형식으로 전처리 해줍니다. 
}

---

## Installation

{}

---

## Getting Started

{contents}

---

## Support and Feedback

{contents}

---

## About Easy Diffuser

{contents}

---

## Licenses

{link to licenses file}

# How To Use Easy Diffuser


## 설치 방법

1. git clone https://github.com/Easy-Diffuser/Model.git 을 하여 해당 프로그램을 Local 컴퓨터에 설치합니다.  

2. 해당 파일에 포함되어 있는 requirements.txt 파일을 pip install -r requirements.txt 명령어를 통해 다운로드합니다. 

3. git lfs install 합니다.

4. git clone https://huggingface.co/leeyunjai/img2txt 저희 모델에 필요한 img2txt 모델을 다운로드 합니다. 

## 사용법

easy_diffuser.py에 정의된 start class를 정의합니다. 

정의한 start class를 통해 class안의 기능들을 사용하면 됩니다. 

개발자 입장에서 이미지를 통해 WEBUI에 사용할 태그를 얻기 위해서는 start.run(img 주소 또는 Link)를 넣으면 됩니다. 이를 통해 객체에는 positive prompt와 negative prompt가 저장이 됩니다. 

어떤 태그들이 저장이 되었는지 확인하기 위해서는 start.print_caption을 실행시키면 됩니다. 

local 저장소에 있는 이미지를 넣는 경우에는 input_img(img)함수를 사용하면 되고 인터넷 링크를 통해 이미지를 넣을 경우는 input_link(link) 함수를 사용하면 됩니다. 

마지막으로 send2ui()함수를 사용하여 이미지를 통해 얻은 태그들을 WEBUI로 보내어 해당 태그와 관련된 이미지를 생성할 수 있습니다.  

