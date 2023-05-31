# HOW TO USE EASY-DIFFUSER

{Logo}


### 생성을 하고 싶은 이미지와 비슷한 Reference 이미지를 사용하여 새로운 이미지 생성에 필요로 하는 알맞은 Postive tag와 Negative tag를 추출합니다. 
### 이를 통해 최소한의 시도로 원하는 이미지를 획득할 수 있도록 도움을 주는 소프트웨어입니다.


# Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Support and Feeback](#support-and-feedback)
5. [About Easy Diffuser](#about-easy-diffuser)
6. [Licenses](#licensed)

---

## Features

 * run_link: 이미지 링크를 삽입하면 해당 이미지와 관련된 Positive prompt와 Negative prompt를 생성합니다.
 * run_image: 이미지 파일을 삽입하면 해당 이미지와 관련된 Positive prompt와 Negative prompt를 생성합니다. 
 * print_caption: run_link 또는 run_image를 통해 생성된 태그들을 출력합니다.
 * send2ui: 생성된 태그들을 WEBUI로 전송합니다. Stable Diffusion이 해당 태그들을 받아 태그와 관련된 이미지를 생성하여 로컬 저장소에 저장합니다. 
 * input_link: 이미지 링크를 삽입하면 모델이 학습할 수 있는 이미지 형식으로 전처리 해줍니다. 

 
---

## Installation


1. git clone https://huggingface.co/leeyunjai/img2txt

2. git clone https://github.com/Easy-Diffuser/Model.git

3. Easy-Diffuser/Model 폴더에 있는 Requirements.txt 파일을 사용하여 소프트웨어 버전을 정의합니다. 

4. webui-user.bat 파일에 set COMMANDLINE_ARGS=--api 해당 코드를 삽입합니다. 

5. 해당 소프트웨어를 사용할 준비가 끝났습니다. 



---

## Getting Started

저희 소프트웨어의 기능을 사용하여 다른 제품을 개발을 하고 싶으시면 아래의 설명을 따르시면 됩니다.

1. 사용할 빈 파일을 생성합니다. 

2. easy diffuser를 import 해줍니다. 

3. easy diffuser에는 start라는 Class가 있습니다. 해당 클래스에는 아래와 같은 메서드들이 있습니다. 

| Function | Function Format | Description |
|--------|----------------|-----------------------------|
|run_link|Class_name.run_link(link)|이미지 링크를 사용하여 이미지와 관련된 Positive prompt와 Negative prompt tag들을 생성합니다.|
|run_img|Class_name.run_img(img)|이미지 파일을 사용하여 이미지와 관련된 Positive prompt와 Negative prompt tag들을 생성합니다.|
|print_caption|Class_name.print_caption()|run_link 또는 run_image를 통해 생성된 태그들을 출력합니다.|
|input_img|Class_name.input_img(img)|local 저장소에 있는 이미지를 클래스 변수에 저장합니다.|
|input_link|Class_name.input_link(link)|link형식의 이미지를 모델이 학습할 수 있는 이미지 형식으로 전처리 해줍니다.|

---

## Support and Feedback

{contents}

---

## About Easy Diffuser

{contents}

---

## Licenses

### https://github.com/Easy-Diffuser/Model/blob/main/LICENSE.md
