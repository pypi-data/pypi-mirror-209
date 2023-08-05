#!/usr/bin/env python3
#from sklearn.preprocessing import MinMaxScaler, StandardScaler
import joblib
import numpy as np
from pkg_resources import resource_filename
import fire, warnings
from dataclasses import dataclass

@dataclass
class Regbot:
  rsi_05: float
  rsi_15: float
  grad_sma25: float
  reg_model_path: str = resource_filename(__name__, 'minute_model.h5')

  def loadmodel(self):
    try:
      return joblib.load(open(f'{self.reg_model_path}', 'rb'))
    except Exception as e:
      return {
        'Error': e
      }


  def prepareInput(self):
    try:
      return np.array([[self.rsi_05,self.rsi_15,self.grad_sma25]])
    except Exception as e:
      return {
        'Error': e
      }


  def buySignalGenerator(self):
    try:
      return (self.loadmodel().predict_proba(self.prepareInput())[:,1])[0]
    except Exception as e:
      return {
        'Error': e
      }



def signal(rsi_05,rsi_15,grad_sma25):
  try:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        return Regbot(rsi_05,rsi_15,grad_sma25).buySignalGenerator()
  except Exception as e:
    return {
      'Error': e
    }


if __name__ == '__main__':
  fire.Fire(signal)
