# StockFlow — Real-Time Stock Market Data Engineering Pipeline

StockFlow is a real-time stock market data engineering pipeline built using Apache Kafka, Python, and AWS cloud services.  
The project demonstrates how streaming financial data can be ingested, processed, stored, and analyzed using scalable event-driven architecture.

---

## Features

- Real-time stock market data streaming using Apache Kafka
- Kafka Producer and Consumer pipeline implementation
- Cloud-based data storage with Amazon S3
- Automated metadata cataloging using AWS Glue
- Serverless analytics using Amazon Athena
- Scalable event-driven data processing workflow

---

## Tech Stack

| Layer | Technology |
|-------|-------------|
| Programming Language | Python |
| Streaming Platform | Apache Kafka |
| Cloud Storage | Amazon S3 |
| Data Cataloging | AWS Glue |
| Query Engine | Amazon Athena |
| Cloud Infrastructure | Amazon EC2 |

---

## Architecture

<img src="Project Architecture.png">

---

## Workflow

1. Stock market data is generated and streamed through Kafka Producers
2. Kafka Consumers process incoming real-time events
3. Processed data is stored in Amazon S3
4. AWS Glue Crawlers catalog the stored datasets
5. Amazon Athena performs analytical queries on processed data

---

## Project Objectives

- Build a scalable real-time data pipeline
- Understand distributed streaming architectures
- Explore cloud-native data engineering workflows
- Implement event-driven data processing concepts

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/shailytech12/StockFlow.git
cd StockFlow
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Kafka & Zookeeper

```bash
# Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka Server
bin/kafka-server-start.sh config/server.properties
```

### 4. Run Producer

```bash
python producer.py
```

### 5. Run Consumer

```bash
python consumer.py
```

---

## License

This project is for educational and learning purposes.
