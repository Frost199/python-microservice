"""
Hotel gateway module
"""
import json
from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class HotelGatewayService:
    """
    A class for the hotel gateway service
    """

    name = "hotel_gateway"

    bookings_rpc = RpcProxy('bookings_service')
    rooms_rpc = RpcProxy('rooms_service')

    @http('GET', '/bookings/<string:booking_id>')
    def get_bookings(self, request, booking_id):
        """
        Get the bookings
        :param request:
        :param booking_id:
        :return:
        """
        booking = self.bookings_rpc.get(booking_id)
        return json.dumps({'booking': booking})

    @http('POST', '/bookings')
    def post_bookings(self, request):
        """
        create a booking
        :param request:
        :return:
        """
        data = json.loads(request.get_data(as_text=True))
        booking_id = self.bookings_rpc.create(data['booking'])

        return booking_id

    @http('GET', '/room/<string:room_id>')
    def get_room(self, request, room_id):
        """
        Get a particular room information
        :param request:
        :param room_id:
        :return:
        """
        room = self.rooms_rpc.get(room_id)
        return json.dumps({'room': room})

    @http('POST', '/room')
    def create_room(self, request):
        """
        Make a room
        :param request:
        :return:
        """
        data = json.loads(request.get_data(as_text=True))
        room_id = self.rooms_rpc.create(data['room_user'], data['room_id'])

        return room_id
