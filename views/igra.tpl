% rebase('base.tpl')

% import model

% if stanje != model.ZMAGA and stanje != model.PORAZ:

    <div>
        <img src="/img/{{igra.stevilo_napak()}}.jpg" />
    </div>

% end

    <div>
        Pravilni del gesla: {{igra.pravilni_del_gesla()}}
    </div>
    
    <div>
        Nepravilne crke: {{igra.nepravilni_ugibi()}}
    </div>

% if stanje == model.ZMAGA:
    <b>Čestitke, zmagal si!</b>
    <form action="/igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>

% elif stanje == model.PORAZ:
    Pravilno geslo: {{igra.geslo}} <br>
    <b>Več sreče prihodnjič</b>
    <form action="/nova_igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>

% else:
    <form method="post" action="/igra/">
        <input name="crka" /> <input type="submit" value="Ugibaj!">
    </form>

% end 
