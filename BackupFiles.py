#from datetime import date
from datetime import datetime, date
from datetime import timedelta
import shutil
import sys

class Backup:
        #Date to day
    today = date.today()    
    Date = today - timedelta(days = 1)    
    Date_transform = today.strftime("%d-%m-%y")
    Date = str(Date)
    Date_transform = str(Date_transform)
    exit_ex = 0

        #Path to find file Matriz
    Path_01 = r'X:\\NFCERESP\\14800340000101\\'
    Path_01 += Date
        #Path to find file Filial
    Path_02 = r'X:\\NFCERESP\\14800340000292\\'
    Path_02 += Date
        #Path to find file Anonio Jorge
    Path_03 = r'X:\\NFCERESP\\13847272000173\\'
    Path_03 += Date    
        #Path to copy files in Hard disk
    dst_01 = r'A:\\BACKUP NFCE GESTAO LOJA01\\NFCE2021\\MARCO\\'
    dst_01 += Date
        
    dst_02 = r'A:\\BACKUP NFCE GESTAO LOJA02\\NFCE2021\\MARCO\\'
    dst_02 += Date

    dst_03 = r'A:\\BACKUP NFCE GESTAO LOJA03\\NFCE2021\\MARCO\\' 
    dst_03 += Date
        #complementation for path in files <expdat.date.dmp.bz2> and <nfe.date.tar.xz>
    expdat = 'expdat.' 
    dmp = '.dmp.bz2'
        
    nfe = 'nfe.'
    tar = '.tar.gz'
        #complementation for files <controle.date.sql.bz2> and <retag.date.sql.bz2>
    controle = 'controle.'
    sql = '.sql.bz2'

    retag = 'retag.'    

        #Path to find files <expdat> and <nfe> in directory
    Path_expdat = r'B:\\'    
    dst_expdat = r'A:\\Backup ERP - RETAGUARDA\\Backup 2021 RETAGUARDA\\MARCO\\'

    Path_nfe = r'B:\\'
    dst_nfe = r'A:\\Backup ERP - RETAGUARDA\\Backup 2021 RETAGUARDA\\MARCO\\'
        
        #Path to find files <controle> and <retag>
    Path_controle = r'X:\\backup\\'
    dst_controle = r'A:\\BACKUP KW - FRENTE LOJA\\KW 2021\\MARCO\\'

    Path_retag = r'X:\\backup\\'
    dst_retag = r'A:\\BACKUP KW - FRENTE LOJA\\KW 2021\\MARCO\\'

        #transform path <expdat> and <nfe>
    Path_expdat += expdat + Date_transform + dmp
    dst_expdat += expdat + Date_transform + dmp

    Path_nfe += nfe + Date_transform + tar
    dst_nfe += nfe + Date_transform + tar

        #transform path <controle> and <retag>
    Path_controle += controle + Date_transform + sql
    dst_controle += controle + Date_transform + sql

    Path_retag += retag + Date_transform + sql
    dst_retag += retag + Date_transform + sql
    
        #Function to copy file Matriz
    def CopyMatriz(self):
        try:                                                            
            shutil.copytree(src=self.Path_01, dst=self.dst_01)
            print('BACKUP DA MATRIZ FOI CONCLUIDO :)\n\n')
            file = open('Rotine_Daily.log', 'a')
                #Date             
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')
                #Matriz
            file.write('Backup Matriz: OK\n')                
            file.write('Nome do arquivo: ')        
            file.write(self.Date)
            file.write('\n')

            file.close()
        except FileExistsError as e:
            print('[MATRIZ] BACKUP JA FOI REALIZADO !!!\n\n')
            file = open('ERRO_Daily.log', 'a')
                #Date        
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')                       
                #Matriz        
            file.write('Erro: Backup Matriz ja foi realizado\n')                
            file.write('\n')

            file.close()
        except PermissionError as e:
            print('[MATRIZ] SEM PERMISSAO PARA ACESSAR O ARQUIVO !!!\n\n')
            file = open('ERRO_Daily.log', 'a')
                #Log files with info for backup        
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')
            file.write('\n')
                #Matriz        
            file.write('Erro: Sem permissao para acessar o arquivo\n')               
            file.write('\n')

            file.close()
        except FileNotFoundError as e:
            print('[MATRIZ] ARQUIVO NAO ENCONTRADO!!!\n\n')
            file = open('ERRO_Daily.log', 'a')            
                #Matriz        
            file.write('   Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')
            file.write('\n')
            file.write('[Matriz]\n')
            file.write('Arquivo nao encontrado :(\n')                
            file.write('\n')

            file.close()
        
    def CopyFilial(self):
        try:            
            print('Data:')
            print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            print('\n\n')

            print('Aguarde estou copiando os arquivos...\n\n')

            shutil.copytree(src=self.Path_02, dst=self.dst_02) 
            print('BACKUP DA FILIAL FOI CONCLUIDO :)\n\n')
            file = open('Rotine_Daily.log', 'a')
                #Date            
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')
            file.write('Backup Filial: OK\n')        
            file.write('Nome do arquivo: ')        
            file.write(self.Date)
            file.write('\n')

            file.close  ()
        except FileExistsError as e:
            print('[FILIAL] BACKUP JA FOI REALIZADO !!!\n\n')
            file = open('ERRO_Daily.log', 'a')                  
                #Filial
            file.write('\n')
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')
            file.write('[Filial]\n')
            file.write('Erro: Backup ja foi realizado\n')        
            file.write('\n')

            file.close()
        except PermissionError as e:
            print('[FILIAL] SEM PERMISSAO PARA ACESSAR O ARQUIVO')
            file = open('ERRO_Daily.log', 'a')
                #Filial        
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')
            file.write('[Filial] \n')
            file.write('Erro: Sem permissao para acessar o arquivo\n')                
            file.write('\n')

            file.close()
        except FileNotFoundError as e:
            print('[FILIAL] ARQUIVO NAO ENCONTRADO')
            file = open('ERRO_Daily.log', 'a')
              #Date        
            file.write('\n')
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))  
            file.write('\n')
                #Matriz        
            file.write('[Filial]\n')
            file.write('Arquivo nao encontrado :(\n')              
            file.write('\n')

            file.close()

    def CopyAntonioJorge(self):
        try:
            shutil.copytree(src=self.Path_03, dst=self.dst_03)           
            file = open('Rotine_Daily.log', 'a')
            file.write('\n')
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')
            file.write('Backup Antonio Jorge: OK\n')
            file.write('Nome do arquivo: ')        
            file.write(self.Date)
            file.write('\n\n')       
            file.close()        
        except FileExistsError as e:           
            file = open('ERRO_Daily.log', 'a')                    
                #Varejao 
            file.write('\n')
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')
            file.write('[Antonio Jorge]\n')
            file.write('Erro: Backup ja foi realizado\n')        
            file.write('\n')
            file.close()
        except FileNotFoundError as e:        
            file = open('ERRO_Daily.log', 'a')
                #Varejao
            file.write('\n')
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')
            file.write('[Antonio Jorge]\n')
            file.write('Arquivo nao encontrado :(\n')               
            file.write('\n')

            file.close()
    def CopyRetaguarda(self):
        try:
            shutil.copy(src=self.Path_expdat, dst=self.dst_expdat)
            shutil.copy(src=self.Path_nfe, dst=self.dst_nfe)
            
            file = open('Rotine_Daily.log', 'a')
            file.write('\n')
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')
            file.write('Backup Retaguarda: OK\n\n')
            file.write('*************************************\n')
            file.write('*************************************\n\n\n')
            file.close()
        except FileExistsError as e:
            file = open('ERRO_Daily.log', 'a')                                  
                #Retaguarda
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')    
            file.write('[Retaguarda]\n')
            file.write('Erro: Backup ja foi realizado\n')                    
            file.write('\n')
            file.write('\n')
            file.close()
        except FileNotFoundError as e:
            print('[RETAGUARDA] ARQUIVO NAO ENCONTRADO !!!\n\n')
            file = open('ERRO_Daily.log', 'a')
            file.write('\n')
                #Retaguarda
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')       
            file.write('[Retaguarda]\n')
            file.write('Arquivo nao encontrado :(\n')               
            file.write('\n')

            file.close()
    def CopyKW(self):
        try:            
            shutil.copy(src=self.Path_controle, dst=self.dst_controle)        
            shutil.copy(src=self.Path_retag, dst=self.dst_retag)        
            
            file = open('Rotine_Daily.log', 'a')
            file.write('\n')
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')
            file.write('Backup KW: OK\n\n')            
            
            file.close()
        except FileExistsError as e:
            file = open('ERRO_Daily.log', 'a')                                  
                #Retaguarda
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')    
            file.write('[KW]\n')
            file.write('Erro: Backup ja foi realizado\n')                    
            file.write('\n')
            file.write('\n')
            file.close()
        except FileNotFoundError as e:
            print('[KW] ARQUIVO NAO ENCONTRADO !!!\n\n')
            file = open('ERRO_Daily.log', 'a')
            file.write('\n')
                #Retaguarda
            file.write('Data: ' )
            file.write(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            file.write('\n')       
            file.write('[KW]\n')
            file.write('Arquivo nao encontrado :(\n')               
            file.write('\n')
BC = Backup()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

BC.CopyFilial()                                                                                                                     
BC.CopyAntonioJorge()
BC.CopyMatriz()
BC.CopyRetaguarda()
BC.CopyKW()