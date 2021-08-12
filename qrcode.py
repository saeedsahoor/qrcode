
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default="",
	help="path to (optional) input video file")

args = vars(ap.parse_args())


vs = VideoStream(args["input"] if args["input"] else 0).start()



while True:

	frame = vs.read()

	barcodes = pyzbar.decode(frame)


	for barcode in barcodes:
        # color  bgr (b,g,r) /// (255,255,255)

		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type

		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)



	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF


	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()
