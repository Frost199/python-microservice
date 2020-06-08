"""
Room gateway module
"""
import uuid

from nameko.rpc import rpc
from nameko_redis import Redis


class RoomService:
    """
    Room service class
    """
    name = "bookings_service"

    redis = Redis('development')

    @rpc
    def get(self, booking_id):
        """
        get a room by id
        :param booking_id:
        :return:
        """
        booking = self.redis.get(booking_id)
        return booking

    @rpc
    def create(self, booking):
        """
        Create a room
        :param booking:
        :return:
        """
        booking_id = uuid.uuid4().hex
        self.redis.set(booking_id, booking)
        return booking_id
