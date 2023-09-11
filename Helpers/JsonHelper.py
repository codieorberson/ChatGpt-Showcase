import json
import csv

class JsonHelper:
    def CsvToJsonl(self, fileName):
        with open(f'TrainingData/{fileName}.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)

            with open(f'TrainingData/{fileName}.jsonl', 'w') as jsonl_file:
                for row in reader:
                    message_data = {
                        "messages": [
                            {"role": "system", "content": row["System"]},
                            {"role": "user", "content": row["User"]},
                            {"role": "assistant", "content": row["Assistant"]}
                        ]
                    }
                    jsonl_file.write(json.dumps(message_data) + '\n')
        
        return True