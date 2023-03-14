python3 -u run_morpher.py morpher_benchmarks/array_add/array_add.c array_add
python3 -u run_morpher.py morpher_benchmarks/array_cond/array_cond.c array_cond
python3 -u run_morpher.py morpher_benchmarks/hpcg/hpcg.c hpcg
python3 -u run_morpher.py morpher_benchmarks/trmm/trmm.c trmm
python3 -u run_morpher.py pace_benchmarks/gemm/gemm_no_unroll_flattened/gemm.c gemm
python3 -u run_morpher.py pace_benchmarks/conv2d/no_unroll_2x2_filt/convolution2d.c convolution2d
python3 -u run_morpher.py pace_benchmarks/conv2d/no_unroll_3x3_filt/convolution2d.c convolution2d
python3 -u run_morpher.py opencgra_benchmarks/fir/kernel.c kernel
python3 -u run_morpher.py cgrame_microbench/sum/sum.c main
python3 -u run_morpher.py cgrame_microbench/mac/mac.c main
python3 -u run_morpher.py cgrame_microbench/mac2/mac2.c main
python3 -u run_morpher.py cgrame_microbench/conv2/conv2.c main
python3 -u run_morpher.py cgrame_microbench/conv3/conv3.c main
