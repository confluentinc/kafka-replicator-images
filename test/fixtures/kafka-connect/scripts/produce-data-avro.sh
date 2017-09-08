#! /bin/bash

rm -f /tmp/test-avro-input.txt

for i in $(seq 10000)
do
echo "{\"id\": $i, \"product\": \"foo\", \"quantity\": 100, \"price\": 50}" >> /tmp/test-avro-input.txt
done

cat /tmp/test-avro-input.txt |
/usr/bin/kafka-avro-console-producer \
  --broker-list "$CONNECT_BOOTSTRAP_SERVERS" --topic "$TOPIC" \
  --property value.schema='{"type":"record","name":"myrecord","fields":[{"name":"id","type":"int"},{"name":"product", "type": "string"}, {"name":"quantity", "type": "int"}, {"name":"price","type": "float"}]}' \
  --property schema.registry.url=http://schema-registry-host:8081/ \
  && echo PASS || echo FAIL
