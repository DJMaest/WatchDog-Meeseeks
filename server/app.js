if (process.env.NODE_ENV !== "production") {
  require("dotenv").config();
}

const express = require('express');
let bodyParser = require("body-parser");
let nodemailer = require('nodemailer');
const app = express();
const port = 3000;

const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/notification', (req, res) => {
    let data = req.body;
    let transporter = nodemailer.createTransport ( {
      host: "smtp.gmail.com",
      port: 465,
      secure: true,
      auth: {
          type: 'OAuth2',
          user: process.env.MAIL_USERNAME,
          pass: process.env.MAIL_PASSWORD,
          clientId: process.env.OAUTH_CLIENTID,
          clientSecret: process.env.OAUTH_CLIENT_SECRET,
          refreshToken: process.env.OAUTH_REFRESH_TOKEN
        }
    });
    
    let mailOptions = {
      from: process.env.MAIL_USERNAME,
      to: `${data.email}`,
      subject: 'Watchdog notification',
      text: 'A suspicious person has been detected near your car'
    };
    
    transporter.sendMail(mailOptions, function(error, info){
      if (error) {
        console.log(error);
      } else {
        console.log('Email sent: ' + info.response);
      }
    });

    client.messages
      .create({
        body: 'Watchdog notification: A suspicious person has been detected near your car',
        from: process.env.TEXT_NUMBER,
        to: `${data.phoneNumber}`
      })
      .then(message => console.log("Text message status: " + message.status));

    res.send("Done");
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});