#!/usr/bin/env python
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START import_libraries]
import argparse
import base64
import os 
#import espeak 
#from espeak import espeak
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
# [END import_libraries]


def main(photo_file):
    """Run a label request on a single image"""

    # [START authenticate]
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)
    # [END authenticate]

    # [START construct_request]
    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [

			{
	    'type': 'IMAGE_PROPERTIES',
                    'maxResults': 1
                	},
		{
                    'type': 'LABEL_DETECTION',
	    'maxResults': 1
		}
		]
            }]
        })
        # [END construct_request]
        # [START parse_response]
        response = service_request.execute()
        label1 = response['responses'][0]['labelAnnotations'][0]['description']
        print('RESPONSE RECEIVED  %s' % (response))
	     
       
        new = './gspch.sh Green value is  ' +str(label1) 
	print('Found label: %s for %s' % (label1, photo_file))
	


# [START run_application]
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    main(args.image_file)
# [END run_application]
