#!/usr/bin/env python
import argparse
import requests
import esrgan_client

def main():
    parser = argparse.ArgumentParser(prog='esrgan', description='Enhance an image using ESRGAN API')
    parser.add_argument('ngrok_url', type=str, help='Ngrok URL of the ESRGAN API')
    parser.add_argument('img_url', type=str, help='URL of the input image')
    parser.add_argument('output_filename', type=str, help='Output filename for the enhanced image')
    args = parser.parse_args()

    esrgan_client.process_image(args.ngrok_url, args.img_url, args.output_filename)

if __name__ == '__main__':
    main()
