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
    name = "rooms_service"

    redis = Redis('development')

    @rpc
    def get(self, room_id):
        """
        get a room by id
        :param room_id:
        :return:
        """
        room = self.redis.hget(room_id)
        return room

    @rpc
    def create(self, room_user, room_number):
        """
        Create a room
        :param room_user:
        :param room_number:
        :return:
        """
        room_id = uuid.uuid4().hex
        self.redis.hmset(room_id, {
            "room_user": room_user,
            "room_number": room_number
        })
        return room_id
