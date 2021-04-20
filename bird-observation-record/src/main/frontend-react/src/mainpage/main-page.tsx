import '../css/main-page.css';
import Cookies from 'js-cookie';
import { UserInfo } from './user-info';
import { Link } from 'react-router-dom';

export const MainPage = () => {

    const title = "Birdy Seoul!!!!";

    return (
        <>
            <body>
                <div>
                    <UserInfo />
                </div>
                <div id="title">
                    <h1>{title}</h1>
                </div>
                <div className="container">
                    <div id="weather">
                    </div>
                    <div id="buttons">
                        <div className="wrap">
                            <button className="button">새들과 산책하기</button>
                        </div>
                        <div className="wrap">
                            <Link to={"/records"}>
                                <button className="button">기록하기</button>
                            </Link>
                        </div>
                        <div className="wrap">
                            <button className="button">기록장 모아보기</button>
                        </div>
                    </div>
                </div>
            </body>
        </>
    );
}