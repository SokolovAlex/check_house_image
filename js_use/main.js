const { torch } = require("js-pytorch");
import * as tf from '@tensorflow/tfjs-node-gpu'

//https://www.tensorflow.org/js/guide/nodejs?hl=ru
const test_model_path = "test/test_model.pt";

const script_module = new torch.ScriptModule(test_model_path);

const model = await tf.loadLayersModel('localstorage://my-model-1');
