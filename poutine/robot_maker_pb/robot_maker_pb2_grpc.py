# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import robot_maker_pb2 as robot__maker__pb2


class RobotMakerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CookRecipe = channel.unary_unary(
                '/protos.RobotMaker/CookRecipe',
                request_serializer=robot__maker__pb2.CookRecipeRequest.SerializeToString,
                response_deserializer=robot__maker__pb2.ListCookRecipeResponse.FromString,
                )


class RobotMakerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CookRecipe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RobotMakerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CookRecipe': grpc.unary_unary_rpc_method_handler(
                    servicer.CookRecipe,
                    request_deserializer=robot__maker__pb2.CookRecipeRequest.FromString,
                    response_serializer=robot__maker__pb2.ListCookRecipeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.RobotMaker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RobotMaker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CookRecipe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.RobotMaker/CookRecipe',
            robot__maker__pb2.CookRecipeRequest.SerializeToString,
            robot__maker__pb2.ListCookRecipeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
