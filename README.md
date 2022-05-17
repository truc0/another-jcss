# Another JCSS

This project is a captcha solver based on [tessereact-ocr](https://tesseract-ocr.github.io/) inspired by [PhotonQuantum/jcss](https://github.com/PhotonQuantum/jcss).

It has lower accurency than [PhotonQuantum/jcss-rs](https://github.com/PhotonQuantum/jcss-rs) but may have higher availability since it works for different image size.

JCSS stands for jAccount Captcha Solver Service.

## Usage

```bash
docker-compose up -d
curl -F "image=@captcha.png" localhost:28888
```
