from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para el menú principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])
        precio_por_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_por_tarro
        
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0
        
        total_con_descuento = total_sin_descuento * (1 - descuento)
        
        return render_template('resultado1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, total_con_descuento=total_con_descuento)
    
    return render_template('ejercicio1.html')

# Ruta para el Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {
        'juan': 'admin',
        'pepe': 'user'
    }
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in usuarios and usuarios[username] == password:
            if username == 'juan':
                return render_template('resultado2.html', mensaje=f'Bienvenido administrador {username}')
            elif username == 'pepe':
                return render_template('resultado2.html', mensaje=f'Bienvenido usuario {username}')
        else:
            return render_template('resultado2.html', mensaje='Usuario o contraseña incorrectos')
    
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)

