#!/usr/bin/env python3
# coding=utf8

def table(hour,weekday):
  work=''
  if weekday == 0:
    if hour % 8 == 0:
      work=list(0)+'+'+list(3)+' 16.3M'+list(13)
    elif hour % 8 == 1:
      work=list(0)+' 5.2M'+list(13)
    elif hour % 8 == 2:
      work=list(5)+' 5.2M'+list(15)
    elif hour % 8 == 3:
      work=list(0)+'+'+list(2)+' 4.24M'+list(15)
    elif hour % 8 == 4:
      work=list(6)+' 5.1'+list(13)
    elif hour % 8 == 5:
      work=list(0)+'+'+list(1)+'+'+list(5)+' 5.1M'+list(15)
    elif hour % 8 == 6:
      work=list(0)+'+'+list(1)+'+'+list(2)+' 5.2M'+list(14)
    elif hour % 8 == 7:
      work=list(0)+' 5.2M'+list(13)
  elif weekday == 1:
    if hour % 8 == 0:
      work=list(0)+' 5.2M'+list(14)
    elif hour % 8 == 1:
      work=list(0)+'+'+list(1)+'+'+list(5)+' 5.1M'+list(15)
    elif hour % 8 == 2:
      work=list(0)+' 5.2M'+list(13)
    elif hour % 8 == 3:
      work=list(7)+' 5.1M'+list(15)
    elif hour % 8 == 4:
      work=list(0)+'+'+list(1)+' 5.2M'+list(14)
    elif hour % 8 == 5:
      work=list(0)+'+'+list(3)+' 16.3M'+list(13)
    elif hour % 8 == 6:
      work=list(0)+'+'+list(1)+' 5.2M'+list(14)
    elif hour % 8 == 7:
      work=list(0)+'+'+list(1)+'+'+list(2)+' 5.2M'+list(13)
  elif weekday == 2:
    if hour % 8 == 0:
      work=list(7)+' 5.1M'+list(15)
    elif hour % 8 == 1:
      work=list(1)+'+'+list(4)+' 15.3M'+list(14)
    elif hour % 8 == 2:
      work=list(6)+' 5.1M'+list(13)
    elif hour % 8 == 3:
      work=list(0)+'+'+list(1)+' 5.2M'+list(14)
    elif hour % 8 == 4:
      work=list(0)+'+'+list(1)+' 5.2M'+list(13)
    elif hour % 8 == 5:
      work=list(6)+' 5.1M'+list(15)
    elif hour % 8 == 6:
      work=list(0)+'+'+list(1)+'+'+list(5)+' 5.1M'+list(15)
    elif hour % 8 == 7:
      work=list(0)+'+'+list(1)+' 5.2M'+list(14)
  elif weekday == 3:
    if hour % 8 == 0:
      work=list(8)+'+'+list(11)+'+'+list(12)+' 3.8M'+list(13)
    elif hour % 8 == 1:
      work=list(8)+'+'+list(9)+' 4M'+list(15)
    elif hour % 8 == 2:
      work=list(10)+'+'+list(11)+'+'+list(12)+' 3.8M'+list(14)
    elif hour % 8 == 3:
      work=list(8)+'+'+list(9)+' 4M'+list(15)
    elif hour % 8 == 4:
      work=list(8)+'+'+list(10)+'+'+list(11)+'+'+list(12)+' 4M'+list(15)
    elif hour % 8 == 5:
      work=list(8)+'+'+list(9)+' 4M'+list(15)
    elif hour % 8 == 6:
      work=list(10)+'+'+list(11)+'+'+list(12)+' 3.8M'+list(14)
    elif hour % 8 == 7:
      work=list(8)+'+'+list(9)+' 4M'+list(15)
  elif weekday == 4:
    if hour % 8 == 0:
      work=list(7)+' 5.1M'+list(15)
    elif hour % 8 == 1:
      work=list(6)+' 5.1M'+list(13)
    elif hour % 8 == 2:
      work=list(0)+'+'+list(1)+'+'+list(5)+' 5.1M'+list(15)
    elif hour % 8 == 3:
      work=list(5)+' 5.2M'+list(15)
    elif hour % 8 == 4:
      work=list(0)+'+'+list(1)+'+'+list(5)+' 5.1M'+list(14)
    elif hour % 8 == 5:
      work=list(0)+'+'+list(2)+' 4.24M'+list(15)
    elif hour % 8 == 6:
      work=list(1)+'+'+list(2)+' 5.2M'+list(14)
    elif hour % 8 == 7:
      work=list(7)+' 5.1M'+list(15)
  elif weekday == 5 or 6:
    if hour % 8 == 0:
      work=list(7)+' 5.1M'+list(15)
    elif hour % 8 == 1:
      work=list(1)+'+'+list(4)+' 15.3M'+list(14)
    elif hour % 8 == 2:
      work=list(0)+'+'+list(3)+' 16.3M'+list(13)
    elif hour % 8 == 3:
      work=list(5)+list(13)+' 5.2M'+list(15)
    elif hour % 8 == 4:
      work=list(0)+'+'+list(1)+'+'+list(5)+' 5.1M'+list(13)
    elif hour % 8 == 5:
      work=list(0)+'+'+list(1)+'+'+list(5)+' 5.1M'+list(13)
    elif hour % 8 == 6:
      work=list(0)+'+'+list(2)+' 4.24M'+list(15)
    elif hour % 8 == 7:
      work=list(1)+'+'+list(2)+' 5.2M'+list(14)
  
  print(work)
  return work



def list(work):
  if work == 0:
    return '建築'
  elif work == 1:
    return '科技'
  elif work == 2:
    return '產兵'
  elif work == 3:
    return '建築加速'
  elif work == 4:
    return '科技加速'
  elif work == 5:
    return '兵加速'
  elif work == 6:
    return '三種加速'
  elif work == 7:
    return '任意加速'
  elif work == 8:
    return '抽卡'
  elif work == 9:
    return '英雄'
  elif work == 10:
    return '分解'
  elif work == 11:
    return '智慧'
  elif work == 12:
    return '殭屍'
  elif work == 13:
    return '  (獎勵: 建)'
  elif work == 14:
    return '  (獎勵: 科)'
  elif work == 15:
    return '  (獎勵: 兵)'
  elif work == 16:
    return ' 16.3M '
  elif work == 17:
    return ' 15.3M '
  elif work == 18:
    return ' 5.2M '
  elif work == 19:
    return ' 5.1M '
  elif work == 20:
    return ' 4M '
  elif work == 21:
    return ' 3.8M '

  
if __name__ == '__main__':
  table(1,0)
