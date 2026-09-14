"""
ٹریڈنگ سٹریٹیجی - Moving Average Strategy
Trading Strategy - Technical Analysis
"""

import pandas as pd
import numpy as np
from ta.trend import EMAIndicator, SMAIndicator

class MovingAverageStrategy:
    """
    Moving Average Crossover Strategy
    جب چھوٹی اوسط لمبی اوسط سے اوپر آئے → خریدیں
    جب چھوٹی اوسط لمبی اوسط سے نیچے جائے → بیچیں
    """
    
    def __init__(self, short_period=10, long_period=30):
        self.short_period = short_period
        self.long_period = long_period
        self.signals = []
        
    def analyze(self, df):
        """
        ڈیٹا کا تجزیہ کریں
        df: pandas DataFrame میں close prices ہوں
        """
        df = df.copy()
        
        # Moving Averages شامل کریں
        df['SMA_SHORT'] = SMAIndicator(
            close=df['close'], 
            window=self.short_period
        ).sma_indicator()
        
        df['SMA_LONG'] = SMAIndicator(
            close=df['close'], 
            window=self.long_period
        ).sma_indicator()
        
        # سگنل بنائیں
        df['SIGNAL'] = 0
        df.loc[df['SMA_SHORT'] > df['SMA_LONG'], 'SIGNAL'] = 1  # خریدیں
        df.loc[df['SMA_SHORT'] < df['SMA_LONG'], 'SIGNAL'] = -1  # بیچیں
        
        # موجودہ سگنل
        current_signal = df['SIGNAL'].iloc[-1]
        
        return {
            'dataframe': df,
            'signal': current_signal,
            'short_ma': df['SMA_SHORT'].iloc[-1],
            'long_ma': df['SMA_LONG'].iloc[-1],
            'current_price': df['close'].iloc[-1]
        }
    
    def get_signal_text(self, signal):
        """سگنل کو اردو میں بتائیں"""
        if signal == 1:
            return "🟢 خریدیں (BUY)"
        elif signal == -1:
            return "🔴 بیچیں (SELL)"
        else:
            return "⚪ انتظار کریں (WAIT)"


class RiskManager:
    """
    خطرات کو سنبھالیں
    """
    
    def __init__(self, take_profit_percent=2.0, stop_loss_percent=1.0):
        self.take_profit_percent = take_profit_percent
        self.stop_loss_percent = stop_loss_percent
    
    def calculate_targets(self, entry_price):
        """
        خریدی ہوئی قیمت سے منافع اور نقصان کا نقطہ نکالیں
        """
        take_profit = entry_price * (1 + self.take_profit_percent / 100)
        stop_loss = entry_price * (1 - self.stop_loss_percent / 100)
        
        return {
            'entry': entry_price,
            'take_profit': take_profit,
            'stop_loss': stop_loss,
            'tp_percent': self.take_profit_percent,
            'sl_percent': self.stop_loss_percent
        }
    
    def check_exit_condition(self, entry_price, current_price):
        """
        چیک کریں کہ نکلنا ہے یا نہیں
        """
        targets = self.calculate_targets(entry_price)
        
        if current_price >= targets['take_profit']:
            return {
                'should_exit': True,
                'reason': f'✅ منافع ہو گیا! {self.take_profit_percent}% اوپر',
                'exit_price': current_price,
                'profit': current_price - entry_price
            }
        
        if current_price <= targets['stop_loss']:
            return {
                'should_exit': True,
                'reason': f'⚠️ رکیں! نقصان {self.stop_loss_percent}% ہو گیا',
                'exit_price': current_price,
                'loss': entry_price - current_price
            }
        
        return {
            'should_exit': False,
            'reason': 'حالت معمول ہے - جاری رکھیں',
            'current_price': current_price
        }
