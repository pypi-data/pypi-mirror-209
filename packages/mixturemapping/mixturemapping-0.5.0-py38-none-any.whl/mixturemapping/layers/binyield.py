## Copyright 2020-2023 Viktor Krueckl. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

_D='OnlyFoolsDoReadThis'
_C='weights'
_B='covariances'
_A='means'
import tensorflow as _tf,numpy as _np
from..binning import BinningScheme
from tensorflow.keras.layers import Layer as _Layer
class BinYieldStatic(_Layer):
	def __init__(A,scheme,**B):A._scheme=scheme;super(BinYieldStatic,A).__init__(**B)
	def build(A,input_shapes):
		B=input_shapes;A._binN=A._scheme.means.shape[0];A._sampleN=A._scheme.means.shape[1];A._outN=A._scheme.means.shape[2];A._2pi_scale=_np.power(2.*_np.pi,A._outN)
		if A._outN!=B[_A][-1]:raise Exception(f"Distribution size ({A._outN}) does not match the integration points  ({B[_A][-1]})!")
		A._means=_tf.expand_dims(_tf.expand_dims(_tf.constant(A._scheme.means.astype(A.dtype)),0),0);A._covariances=_tf.expand_dims(_tf.expand_dims(_tf.linalg.diag(_tf.constant(A._scheme.covariances.astype(A.dtype))),0),0);A._weights=_tf.expand_dims(_tf.expand_dims(_tf.constant(A._scheme.weights.astype(A.dtype)),0),0);super(BinYieldStatic,A).build(B)
	def call(A,x,**I):C=_tf.expand_dims(_tf.expand_dims(x[_A],2),2)-A._means;D=_tf.expand_dims(_tf.expand_dims(x[_B],2),2)+A._covariances;E=_tf.linalg.pinv(D);F=_tf.sqrt(_tf.linalg.det(D)*A._2pi_scale);G=-.5*_tf.reduce_sum(C*_tf.linalg.matvec(E,C),4);B=_tf.exp(G)/F;B=B*A._weights*_tf.expand_dims(_tf.expand_dims(x[_C],-1),-1);H=_tf.minimum(_tf.reduce_sum(_tf.reduce_sum(B,3),1),1.,name=_D);return H
	def compute_output_shape(A,input_shape):return input_shape[0],A._binN
class BinYield(_Layer):
	def __init__(A,**B):super(BinYield,A).__init__(**B)
	def build(A,input_shapes):super(BinYield,A).build(input_shapes)
	def call(D,x,**O):E=_tf.cast(_tf.shape(x[_A])[2],D.dtype);F=_tf.math.pow(_tf.constant(2.*_np.pi),E);G=_tf.expand_dims(x['bin_means'],1);H=_tf.expand_dims(_tf.linalg.diag(x['bin_covariances']),1);I=_tf.expand_dims(x['bin_weights'],1);B=_tf.expand_dims(_tf.expand_dims(x[_A],2),2)-G;C=_tf.expand_dims(_tf.expand_dims(x[_B],2),2)+H;J=_tf.expand_dims(_tf.expand_dims(x[_C],-1),-1);K=_tf.linalg.pinv(C);L=_tf.sqrt(_tf.linalg.det(C)*F);M=-.5*_tf.reduce_sum(B*_tf.linalg.matvec(K,B),4);A=_tf.exp(M)/L;A=A*I*J;N=_tf.minimum(_tf.reduce_sum(_tf.reduce_sum(A,3),1),1.,name=_D);return N