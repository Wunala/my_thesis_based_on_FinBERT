#!/usr/bin/env bash

python3.6 run_classifier.py \
  --data_dir=data \
  --task_name=sim \
  --vocab_file=FinBERT_L-12_H-768_A-12_tf/vocab.txt \
  --bert_config_file=FinBERT_L-12_H-768_A-12_tf/bert_config.json \
  --output_dir=sim_model \
  --do_train=true \
  --do_eval=true \
  --init_checkpoint=FinBERT_L-12_H-768_A-12_tf/bert_model.ckpt \
  --max_seq_length=72 \
  --train_batch_size=32 \
  --learning_rate=5e-5 \
  --num_train_epochs=3.0
