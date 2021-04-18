import ReactDOM from 'react-dom';
import './index.css';
import { BrowserRouter, Route } from 'react-router-dom';
import reportWebVitals from './reportWebVitals';
import { MainPage } from './mainpage/main-page';
import { LoginPage } from './mainpage/login-page';
import { RegisterPage } from './mainpage/register-page';
import axios from 'axios';

axios.defaults.baseURL = "http://localhost:3000";
axios.defaults.withCredentials = true;

ReactDOM.render(
  <BrowserRouter>
    <div>
      <Route path="/" component={MainPage} exact={true} />
      <Route path="/records" component={() => <div>관차라라라라라라</div>}/>
      <Route path="/login" component={LoginPage} />
      <Route path="/register" component={RegisterPage} />
    </div>
  </BrowserRouter>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
