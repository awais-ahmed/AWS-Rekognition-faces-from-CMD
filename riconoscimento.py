import sys
import urllib.request
import boto3
import io
import json

#Cerca facce (Predict)
def search_face_in_image(url):
    threshold = 50
    maxFaces = 1
    collectionId_sfii = ""
    rekognition_client = boto3.client('rekognition',aws_access_key_id='',
                                      aws_secret_access_key = '',
                                      region_name = '')
    with urllib.request.urlopen(url) as url:##con url
        imagebytes = io.BytesIO(url.read())##
    #with open(imagesbytes, 'rb') as imagebytes: ### path
        response = rekognition_client.search_faces_by_image(CollectionId=collectionId_sfii,
                                Image={"Bytes": imagebytes.read()},
                                FaceMatchThreshold=threshold,
                                MaxFaces=maxFaces)
        print("\nResponse:")
        faceMatches = response['FaceMatches']
        lenght = (len(faceMatches))
        response = json.dumps(response, sort_keys=True, indent=4)
        print(response)
        print("---------------------O_O---------------------")

        if lenght == 0:
            print("Non sono riuscito a riconoscere la faccia, aggiungerla alla collezione!")
        else:
            for match in faceMatches:
                print('ExternaImageId--> Nome: ' + match['Face']['ExternalImageId'])
                print('FaceId--> ID:' + match['Face']['FaceId'])
                print('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")

if __name__ == '__main__':
    search_face_in_image(sys.argv[1])