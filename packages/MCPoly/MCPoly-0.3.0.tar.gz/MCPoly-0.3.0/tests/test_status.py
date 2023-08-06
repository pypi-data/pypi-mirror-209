from MCPoly.status import status
from MCPoly.status import echart
from MCPoly import view3d
import pytest
import os
import re

@pytest.fixture
def current1():
    return status('Atoms1',loc='./data_status/')

def test1_status_status1(current1):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current1.status(figureonly=True)
    os.chdir(opath)
    assert len(num)==8

def test2_status_status1(current1):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current1.status(figureonly=True)
    os.chdir(opath)
    for E in num:
        assert E<=-1150.90
        
@pytest.fixture
def current1():
    return status('Atoms1',loc='./data_status/')

def test1_status_statusonly1(current1):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current1.status(figureonly=True,statusonly=True)
    os.chdir(opath)
    assert num==2
    
def test2_status_statusonly1(current1):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current1.energy()
    os.chdir(opath)
    assert num==-1150.932617

def test3_status_statusonly1(current1):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current1.gibbs()
    os.chdir(opath)
    assert num==-1150.919111
    
@pytest.fixture
def current2():
    return status('Atoms2',loc='./data_status/')

def test_status_statusonly2(current2):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current2.status(figureonly=True,statusonly=True)
    os.chdir(opath)
    assert num==1

@pytest.fixture
def current3():
    return status('Atoms3',loc='./data_status/')

def test_status_statusonly3(current3):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current3.status(figureonly=True,statusonly=True)
    os.chdir(opath)
    assert num==0

@pytest.fixture
def current4():
    return status('Atoms4',loc='./data_status/')

def test_status_status4(current4):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current4.status(figureonly=True)
    os.chdir(opath)
    assert len(num)==78

@pytest.fixture
def current4():
    return status('Atoms4',loc='./data_status/')

def test_status_statusonly4(current4):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current4.status(figureonly=True,statusonly=True)
    os.chdir(opath)
    assert num==4

@pytest.fixture
def current1():
    return status('Atoms1',loc='./data_status/')

def status_figure(current1):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    current1.figure(7)
    os.chdir(opath)
    return 0

@pytest.fixture
def current1():
    return status('Atoms1',loc='./data_status/')

def status_figureonly(current1):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    current1.figuretraj()
    os.chdir(opath)
    return 0

@pytest.fixture
def current5():
    return ['Atoms1','Atoms5']

def test1_status_echart(current5):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    data=echart(files=current5,loc='./data_status/',fig_pattern='line',hartree=True,absolute=True,figdata=True,savefig=False,xx=True)
    assert data==[-1150.932617,-995.394366]
    f=open('./data_status/Result.csv','r')
    a0=0
    a1=0
    for line in f:
        a=re.search('Step,File,∆E\(Eh\)',line)
        if a:
            a0=1
        b=re.search('1,Atoms5,-995.394366',line)
        if b:
            a1=1
    os.chdir(opath)
    assert a0*a1==1

def test2_status_echart(current5):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    data=echart(files=current5,loc='./data_status/',energy_pattern='Gibbs',fig_pattern='bar',hartree=False,absolute=False,figdata=True,savefig=False,dataname='Result2',xx=True)
    assert data==[0.,97752.61908948798]
    f=open('./data_status/Result2.csv','r')
    a0=0
    a1=0
    for line in f:
        a=re.search('Step,File,∆G\(kcal/mol\)',line)
        if a:
            a0=1
        b=re.search('1,Atoms5,97752.61908948798',line)
        if b:
            a1=1
    os.chdir(opath)
    assert a0*a1==1