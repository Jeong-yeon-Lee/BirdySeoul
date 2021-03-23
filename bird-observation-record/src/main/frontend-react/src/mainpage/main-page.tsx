import { Link, Route } from 'react-router-dom';
import '../css/main-page.css';

export const MainPage = () => {
    return (
        <body>
            <Route path="/records" component= {() => <div>관차라라라라랄!</div>} exact={true}/>
            <div id="title">
                <h1>Birdy Seoul</h1>
            </div>
            <ul>
                <li>
                    <Link to="/records">관찰목록</Link>
                </li>
            </ul>
            <div className="container">
                <div id="weather">
                </div>
                <div id="buttons">
                    <div className="wrap">
                        <button className="button">새들과 산책하기</button>
                    </div>
                    <div className="wrap">
                        <button className="button">기록하기</button>
                    </div>
                    <div className="wrap">
                        <button className="button">기록장 모아보기</button>
                    </div>
                </div>
            </div>
        </body>
    );
}