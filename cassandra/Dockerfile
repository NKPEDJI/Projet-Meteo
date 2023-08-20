# Use the official Cassandra image
FROM cassandra:latest

# Expose the required ports for Cassandra
EXPOSE 9042 9160

# Copy any custom configuration files if needed
COPY cassandra-config-file.conf /etc/cassandra/

# The CMD instruction is already set in the official Cassandra image
# CMD ["cassandra", "-f"]
