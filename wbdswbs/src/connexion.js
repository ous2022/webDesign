// import { Fragment } from "react"

import { Link } from "react-router-dom"

const Connexion = () => {
    return( 
        <div className='connect'>
            <div className="left">
                <h1>Connexion</h1>
                <p>
                    Connectez-vous ici pour acceder à notre site dans son integralité
                </p>

                <form>
                    <div className="email">
                        <label htmlFor="email">Email</label>
                        <input type="email" id="email" name="email" />
                    </div>
                    <div className="password">
                        <label htmlFor="password">Mot de passe</label>
                        <input type="password" id="password" name="password" />
                    </div>

                    <div className="btn">
                        <button type="submit">Se connecter</button>
                    </div>
                </form>
                <span>
                    Vous n'avez pas de compte ? <Link className="toco" to="/inscription">Inscrivez vous</Link>
                </span>
            </div>

            <div className="right">
                <img src="" alt="" />
            </div>
        </div>
    )
}

export default Connexion