import sender_stand_request
import data


def post_new_order_step():
    user_response = sender_stand_request.post_new_order(data.order_body)
    return user_response.json()["track"]

def get_order_by_track_step(track):
    user_response = sender_stand_request.get_order_by_track(track)
    return user_response
def positive_assert_step(order):
    assert order.status_code == 200
def test_order_data_by_track_allowed():
    track = post_new_order_step()
    order = get_order_by_track_step(track)
    positive_assert_step(order)

