css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #000
}
.chat-message .avatar {
  width: 10%;
}
.chat-message .avatar img {
  max-width: 48px;
  max-height: 48px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn.discordapp.com/attachments/923227434168492132/1206913205658460220/APmgjFvDIjjh1pTRRmqhU1SmgHhZmBWCnKYutYmulcE9WqEmpRpbHpHXJj3ONWCEBi0rsdDcEL0qSB7ch6XMPHLA3a582MOp4D7Q2hjz59a0PlWPnb6yNC80HwMmjJWa1LlHyiPWacL3xBg92VXefDYT_wZLs_IOMYBoSX5xG5cG0hUrEHhSLfkpDDMQJHETnwZATWTwYWiqPXOKJGrn23iPdbVg54Ch_AooEtl-DX5yc2cffJO4wTf2fON8GebrmIMg53IpEAw_UsmmQ9Fs5ZeIe_IRBiJmwERwtkd41yBNVUAWMQzQhpB_3TG-WMKWvMuoH47DNemZg_XfCCRdkjY.png?ex=65ddbc83&is=65cb4783&hm=ffaed9aafcfe068f8313d60d8c428ee791a705d674cb7f82e47d244950371903&" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn.discordapp.com/attachments/836301257831612428/1206914152522584084/Untitled_design_5.png?ex=65ddbd65&is=65cb4865&hm=fc7b899e799d4dfa44af7952d0e86c04655d4e3ae312bc6e3336ae9c513dab05&">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''