"""
MQTT Wrapper from viso.ai
"""

import threading
import time
from typing import Any, Optional, Union
from paho.mqtt.client import Client

from viso_sdk.constants import PREFIX
from viso_sdk.logging import get_logger


logger = get_logger("MQTT")


class MqttWrapper(threading.Thread):
    """Represents a Viso MQTT related API instance

    You can execute your callback function when a message is received from a topic.
    To do this, use `callbacks` parameter to define callback(s) of topic(s):

    .. highlight:: python
    .. code-block:: python

        def on_message(msg):
            # This function is called when a message is arrived on "my_topic" topic.
            print(f"Message arrived - {msg}")

        mqtt_client = VisoMQTT(callbacks={"my_topic" : on_message, "topic2": callback2})

    Args:
        host(str): Host of the MQTT broker.  Normally 127.0.0.1
        port(int): Port of the MQTT broker.  Default value is 1883
        callbacks(dict): Callback dictionary. Contains `topic: callback` pairs.
        verbose(bool): Use verbose logging or not
    """

    def __init__(
            self,
            host: Optional[str] = "127.0.0.1",
            port: Optional[int] = 1883,
            callbacks: Optional[Union[dict, None]] = None,
            verbose: Optional[bool] = True,
    ):
        super().__init__()
        self.callbacks: dict = callbacks or {}
        self.host = host
        self.port = port
        self._client: Client = Client()
        self._client.on_connect = self._on_mqtt_connected
        self._client.on_message = self._on_mqtt_message
        self._b_stop = threading.Event()
        self._b_stop.clear()
        self.verbose = verbose
        self.start()

    @staticmethod
    def gen_mqtt_key_local(node_id, port):
        return f"{PREFIX.MQTT.LOCAL}_{node_id}_{port}"

    @staticmethod
    def gen_mqtt_key_cloud(node_id, port):
        return f"{PREFIX.MQTT.CLOUD}_{node_id}_{port}"

    @staticmethod
    def gen_mqtt_key_debug(node_id, port):
        return f"{PREFIX.MQTT.DEBUG}_{node_id}_{port}"

    def connect(self) -> bool:
        """Connect to the target MQTT broker"""
        try:
            self._client.connect(self.host, self.port)
        except Exception as err:
            logger.error(f"Failed to connect to {self.host}:{self.port} - {err}")
            return False
        self._client.loop_start()
        return True

    def run(self) -> None:
        """Main thread loop"""
        while not self._b_stop.is_set():
            # Check MQTT connection and connect if not.
            if not self._client.is_connected():
                self.connect()
            time.sleep(1)

    def _on_mqtt_connected(self, *args: Any) -> None:
        """Callback when MQTT is connected"""
        logger.info(f"Connected to the MQTT broker - {args}")
        if args[-1] == 0:  # Check ResultCode
            for topic in self.callbacks.keys():
                self._client.subscribe(topic=topic)

    def _on_mqtt_message(self, *args: Any) -> None:
        """Callback when a message on subscribed channels is received."""
        topic = args[2].topic
        msg = args[2].payload.decode("utf-8")
        if self.verbose:
            logger.debug(f"Received a message(`{msg}`) on topic: `{topic}`")
        if callable(self.callbacks.get(topic)):
            # Call corresponding callback function with the message payload as an argument.
            self.callbacks[topic](msg)
        else:
            logger.error(f"Callback of topic '{topic}' is not callable!")

    def publish(self, topic: str, payload: str) -> None:
        """Publish a message to a topic"""
        self._client.publish(topic=topic, payload=payload)

    def stop(self) -> None:
        """Stop this thread"""
        self._b_stop.set()
