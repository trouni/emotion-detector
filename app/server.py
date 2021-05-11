import responder
import time
from io import BytesIO
# import aiohttp
# from fastai import *
# from fastai.vision import *

api = responder.API()

# path = Path("data")
classes = [
    'anger',
    'contempt',
    'disgust',
    'fear',
    'happiness',
    'neutral',
    'sadness',
    'surprise'
]
# data = DataBunch.load_empty(path)

# learn = cnn_learner(data, models.resnet34)
# learn.load("model")


# async def get_bytes(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.read()


@api.route("/")
def index(request, response):
    response.media = {'hello': 'world'}


@api.route("/classify-url")
async def classify_url(request, response):

    def predict_emotion(data):
        time.sleep(2)
        return {
            "prediction": 'test-prediction',
            "scores": ['test', 'scores']
        }
        # img = open_image(BytesIO(bytes))
        # _, class_, losses = learn.predict(img)
        # return {
        #     "prediction": classes[class_.item()],
        #     "scores": sorted(
        #         zip(learn.data.classes, map(float, losses)),
        #         key=lambda p: p[1],
        #         reverse=True
        #     )
        # }
        # print(result)


    # Parse the incoming data as form-encoded.
    data = await request.media()

    # Process the data (in the background).
    result = predict_emotion(data)
    # Immediately respond that upload was successful.
    response.media = result

if __name__ == '__main__':
    api.run()
