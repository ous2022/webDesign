const Inscription = () => {
    return(
        <div className="connect">
            <div className="left">
                <h1>Inscription</h1>
                <p>
                    Inscrivez-vous ici pour acceder à notre site dans son integralité
                </p>

                <form>
                    <div className="nom">
                        <label htmlFor="nom">Nom Complet</label>
                        <input type="nom" id="nom" name="nom" />
                    </div>
                    <div className="email">
                        <label htmlFor="email">Email</label>
                        <input type="email" id="email" name="email" />
                    </div>
                    <div className="numero">
                        <label htmlFor="numero">Numero de telephone</label>
                        <input type="numero" id="numero" name="numero" />
                    </div>
                    <div className="password">
                        <label htmlFor="password">Mot de passe</label>
                        <input type="password" id="password" name="password" />
                    </div>

                    <div className="btn">
                        <button type="submit">Se connecter</button>
                    </div>
                </form>
            </div>

            <div className="right">
                <img src="https://i.imgur.com/6Q7b3Z9.png" alt="" />
            </div>

        </div>
    )
}

export default Inscription