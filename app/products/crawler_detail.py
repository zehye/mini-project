import urllib.request
import json


class GetExhibitionDetail:
    def __init__(self, no):
        self.no = no

    def get_exhibition_detail(self):
        param = {
            'no': self.no,
        }
        response = urllib.request.urlopen(
            'https://api.booking.naver.com/v3.0/businesses/', param)
        data = json.load(response)

        exhibition_detail_list = list()
        exhibition_detail_dict = dict()

        title = data['serviceName']
        sm_title = data['desc']
        description = data['promotionDesc']
        address = data['addressJson']['address']
        photo_desc = data['extraDescJson'][0]['images'][0]['src']

        exhibition_detail_dict['title'] = title
        exhibition_detail_dict['sm_title'] = sm_title
        exhibition_detail_dict['description'] = description
        exhibition_detail_dict['address'] = address
        exhibition_detail_dict['photo_desc'] = photo_desc

        exhibition_detail_list.append(exhibition_detail_dict)
        return exhibition_detail_list

    def get_exhibition_review(self):
        param = {
            'no': self.no,
        }
        response = urllib.request.urlopen(
            'https://api.booking.naver.com/v3.0/businesses/reviews?', param)
        datas = json.load(response)

        exhibition_detail_review_list = list()
        for data in datas:
            account = data['account']
            score = data['score']
            body = data['body']
            usedate = data['useDate']

            exhibition_detail_review_dict = dict()
            exhibition_detail_review_dict['account'] = account
            exhibition_detail_review_dict['score'] = score
            exhibition_detail_review_dict['body'] = body
            exhibition_detail_review_dict['usedate'] = usedate

            exhibition_detail_review_list.append(exhibition_detail_review_dict)
        return exhibition_detail_review_list




