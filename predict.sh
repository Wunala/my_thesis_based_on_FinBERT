#!/usr/bin/env bash
python3.6 run_classifier.py \
  --task_name=sim \
  --do_predict=true \
  --data_dir=data \
  --vocab_file=FinBERT_L-12_H-768_A-12_tf/vocab.txt \
  --bert_config_file=FinBERT_L-12_H-768_A-12_tf/bert_config.json \
  --init_checkpoint=tmp/sim_model \
  --max_seq_length=128 \
  --output_dir=output

