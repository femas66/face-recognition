import face_recognition
import os

def main():
  my_photo_path = 'images/femas2.jpg'
  unknown_path = 'images/unknown.jpg'
  if not os.path.isfile(my_photo_path) or not os.path.isfile(unknown_path):
    print("file tidak ada")
    exit()
  my_photo = face_recognition.load_image_file(my_photo_path)
  my_photo_encoding = face_recognition.face_encodings(my_photo)[0]
  
  unknown = face_recognition.load_image_file(unknown_path)
  unknown_encoding = face_recognition.face_encodings(unknown)[0]
  
  result: bool = face_recognition.compare_faces([my_photo_encoding], unknown_encoding)
  if result:
    print(f"Foto '{my_photo_path}' SAMA dengan '{unknown_path}'")
  else:
    print(f"Foto '{my_photo_path}' TIDAK SAMA dengan '{unknown_path}'")
  
  
if __name__ == '__main__':
  main()