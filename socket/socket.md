# socket  

ソケット通信  

- TCP  
  - 信頼性が高い、確認あり  
  - コネクション型  
  - ストリーム（SOCK_STREAM）  
  - 1対1 のみ  
  - サーバ側 / クライアント側（Client → Server）  
    - TCP-Server-01.py（1度送ったら終わり）  
    - TCP-Client-01.py（受信し続ける）  

- UDP  
  - 信頼性を担保する仕組みがない、確認なし  
  - コネクションレス型  
  - 処理が簡単で遅延が少ない  
  - データグラム（SOCK_DGRAM）  
  - 1対多も可能  
  - 送信側 / 受信側（Sender → Reciver）  
    - UDP-Sender-01.py  
    - UDP-Reciever-01.py


---  

---  

### reference  

[https://qiita.com/msrks/items/0550603efc59f6e8ba09](https://qiita.com/msrks/items/0550603efc59f6e8ba09)  

[http://memo.saitodev.com/home/python_network_programing/](http://memo.saitodev.com/home/python_network_programing/)

