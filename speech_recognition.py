"""Sequence-to-sequence model with an attention mechanism."""
from __future__ import print_function
import numpy as np
import tensorflow as tf
import layer
import speech_data
from speech_data import Source,Target
from layer import net

learning_rate = 0.00001
training_iters = 300000 #steps
batch_size = 64



input_classes=20 # mfcc features
max_input_length=80 # (max) length of utterance
max_output_length=20
output_classes=32 # dimensions: characters



batch=word_batch=speech_data.mfcc_batch_generator(batch_size, source=Source.DIGIT_WAVES, target=Target.hotword)
X,Y=next(batch)



vocab_size=input_classes
target_vocab_size=output_classes
buckets=[(max_input_length, max_output_length)]
PAD=[0]

input_data    = x= X
target_data   = y= Y
target_weights= [[1.0]*50 + [0.0]*(max_input_length-50)] *batch_size # mask padding. todo: redundant --
encoder_size = max_input_length
decoder_size = max_output_length

num_dim=input_classes

def res_block(tensor, size, rate, dim=num_dim):
    # filter convolution
    conv_filter = tensor.sg_aconv1d(size=size, rate=rate, act='tanh', bn=True)
    # gate convolution
    conv_gate = tensor.sg_aconv1d(size=size, rate=rate,  act='sigmoid', bn=True)
    # output by gate multiplying
    out = conv_filter * conv_gate
    # final output
    out = out.sg_conv1d(size=1, dim=dim, act='tanh', bn=True)
    # residual and skip output
    return out + tensor, out


z = x.sg_conv1d(size=1, dim=num_dim, act='tanh', bn=True)


skip = 0  # skip connections
for i in range(num_blocks):
    for r in [1, 2, 4, 8, 16]:
        z, s = res_block(z, size=7, rate=r)
        skip += s

logit = (skip
         .sg_conv1d(size=1, act='tanh', bn=True)
         .sg_conv1d(size=1, dim=voca_size))


loss = logit.sg_ctc(target=y, seq_len=seq_len)
tf.train.AdamOptimizer(learning_rate).minimize(loss)
saver = tf.train.Saver(tf.global_variables())


tf.sg_train(log_interval=30, lr=0.0001, loss=loss, ep_size=1000, max_ep=200, early_stop=False)




class SpeechSeq2Seq(object):

	def __init__(self,size, num_layers):

		cell = single_cell = tf.nn.rnn_cell.GRUCell(size)
		if num_layers > 1:
		 cell = tf.nn.rnn_cell.MultiRNNCell([single_cell] * num_layers)
		# Feeds for inputs.
		self.encoder_inputs = []
		self.decoder_inputs = []
		self.target_weights = []
		i=0
		self.encoder_inputs.append(tf.placeholder(tf.int32, shape=[None], name="encoder{0}".format(i)))
		self.decoder_inputs.append(tf.placeholder(tf.int32, shape=[None], name="decoder{0}".format(i)))
		self.target_weights.append(tf.placeholder(tf.float32, shape=[None], name="weight{0}".format(i)))
		# tf.nn.rnn()
		# targets = [self.decoder_inputs[i + 1] for i in xrange(len(self.decoder_inputs) - 1)]
		self.outputs, self.losses = tf.nn.seq2seq.basic_rnn_seq2seq(encoder_inputs, decoder_inputs, cell)
		tf.train.AdamOptimizer(learning_rate).minimize(self.losses)
		self.saver = tf.train.Saver(tf.all_variables())

	# def step(self, session, encoder_inputs, decoder_inputs, target_weights, test):
		pass
def test():
	perplexity, outputs = model.step(session, input_data, target_data, target_weights, test=True)
	words = np.argmax(outputs, axis=2)  # shape (10, 10, 256)
	# word = decode(words[0])
	word = str(words[0])
	print("step %d, perplexity %f, output: hello %s?" % (step, perplexity, word))

def train():
	step=0
	test_step=1
	with tf.Session() as session:
		model= SpeechSeq2Seq(size=10, num_layers=1)
		session.run(tf.initialize_all_variables())
		while True:
			model.step(session, input_data, target_data, target_weights, test=False) # no outputs in training
			if step % test_step == 0:
				test()
			step=step+1
