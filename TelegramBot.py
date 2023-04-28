import telebot
import Config
import serial
import subprocess
import random

bot = telebot.TeleBot(Config.TOKEN)

                # -------------------------------------- VARIABLES -------------------------------------- #

respuesta = [
'Es cierto.', 
'Es decididamente así.', 
'Sin lugar a dudas.', 
'Sí, definitivamente.', 
'Puedes confiar en ello', 
'Como yo lo veo, sí.', 
'Lo más probable.', 
'Perspectiva buena.', 
'Sí.', 
'Las señales apuntan a que sí.', 
'Respuesta confusa, vuelve a intentarlo.', 
'Vuelve a preguntar más tarde.', 
'Mejor no decirte ahora.', 
'No se puede predecir ahora.', 
'Concéntrate y vuelve a preguntar.', 
'No cuentes con ello.', 
'Mi respuesta es no.', 
'Mis fuentes dicen que no.', 
'Las perspectivas no son muy buenas.', 
'Muy dudoso.'
]


chistes = ["Este era un chiste tan malo, pero tan malo, que pegaba a todos los chistes más pequeños que él.", "¡Capitán, capitán! Están a punto de atacarnos 40 carabelas. ¿Una flota? No, flotan todas.", "Jaimito, puedes definir el término telepatía. Pues es una tele para la hermana de mi mamá.", "¿Sabes cómo se queda un mago después de comer? Magordito.", "Carlitos, puedes decirme una palabra que tenga muchas “o”. Muy fácil maestra, ¡Gooooooool!", "¿Por qué las focas en el espectáculo siempre miran hacia arriba? Porque es donde se encuentran los focos.",  "Buenas tardes, ¿me gustaría alquilar un “Batman Forever”? No es posible, tienes que devolverlo tomorrow.",  "¿Qué le dice un techo a otro? Techo de menos.",  "Donald usa teclado y Mickey mouse.",  "Jaimito, ¿qué harías si te estuvieses ahogando en el mar? Pues llorar mucho para desahogarme.",  "Un niño llama a la lavandería y pregunta: ¿ahí es donde lavan la ropa? No, le contestan del otro lado del teléfono. Pues que sucios sois.",  "Hola, ¿está Agustín? No, estoy incomodín.",  "¿Cómo sube Thor a un rascacielos? Pues en un ElevaThor.",  "¿Por qué el volcán está considerado como la montaña más limpia? Porque echa cenizas y después lava.", "Mamá, ¿cómo se dice perro en inglés? Dog. Y veterinario. Pues Dog-tor.", "¿Cuál es la fruta más divertida? Sin duda, la naranjajajajaja", "¿Qué le regaló Batman a su mamá por su cumpleaños? Una Bat-idora.", "Carlitos, ¿puedes decirme dos palabras que tengan tilde? Muy sencillo, maestra: Matilde y Clotilde.", "¡Profesora! Acaban de robarme en el pasillo. No me digas, ¿y qué te robaron, Jaimito? Pues los deberes.", "¿Qué le dice una iguana a su hermana gemela? Somos iguanitas.", "¡Me acaba de morder una serpiente! ¿Cobra? No, por suerte fue gratis.", "¿Cuál es el colmo de un futbolista? Que le hagan la pelota.", "Juanito, ve corriendo a la cocina que las lentejas se están pegando. Mamá, lo siento, pero me has enseñado a no meterme en peleas ajenas.", "¿Qué le dice un gusano a otro? Me voy a dar la vuelta a la manzana.", "¿Qué es un pez en un cine? Un mero espectador.", "¿Por qué se suicidó el libro de matemáticas? Porque tenía muchos problemas por resolver.", "¿Por qué a los esqueletos no les gusta la lluvia y el frío? Porque se calan hasta los huesos.", "Pepito, ¿por qué tu redacción sobre la leche te ha quedado tan corta? Porque hablo de la leche condensada maestra.", "Si los zombies se degradan con el paso del tiempo, entonces son ¿zombiodegradables?", "Buenos días, ¿tienen libros sobre el cansancio? Sí, pero ahora mismo están todos agotados.", "Jaimito, ¿qué harías si te estuvieras ahogando en alta mar? ¡Llorar para desahogarme!", "¡Papá, papá! ¿Puedo ir al cine? Sí, Jaimito, pero no entres.","¿Qué hace una persona con un sobre de kétchup en la oreja? Escuchando salsa.", "¿Cómo se despiden los químicos? Ácido un placer.", "¿Sabes qué? Mi hermano va en bicicleta desde los 4 años. ¡Pues sí que debe estar lejos!", "¿Cuál es el colmo de un jardinero? Que siempre le dejen plantado.", "¿Qué le dice un ganso a una gansa? ¡Ven-gansa!", "¿Ey, cómo se escribe nariz en inglés? Nose ¿Tú tampoco lo sabes?", "Soy muy saludable. Ah. ¿Comes sano y todo eso? No, digo que la gente me saluda.", "¿Tienes WiFi? Sí. ¿Y cuál es la clave? Tener dinero y pagarlo.", "¿Por qué las focas del circo miran siempre hacia arriba? Porque es donde están los focos.", "Buenos días, me gustaría alquilar “Batman Forever”. No es posible, tiene que devolverla tomorrow.", "¿Qué le dice un techo a otro? Techo de menos.", "Buenos días. Busco trabajo. ¿Le interesa de jardinero? ¿Dejar dinero? ¡Si lo que busco es trabajo!", "¡Rápido, necesitamos sangre! Yo soy 0 positivo. Pues muy mal, aquí se viene a animar.", "¿Cómo queda un mago después de comer? ¡Magordito!", "Robinson Cruzó… y lo atropellaron.", "¿Qué hace un perro con un taladro? Taladrando.", "¿Sabes por qué no se puede discutir con un DJ? Porque siempre están cambiando de tema.", "¿Qué le dice una impresora a otra? Esa hoja es tuya o es impresión mía.","¿Qué le dice un techo a otro? Techo de menos.", "Doctor, nadie me hace caso...¡Que pase el siguiente!", "Se sube un señor al autobús y le pregunta al conductor: ¿Cuánto vale el bus? Un euro. Pues que se bajen todo el mundo, que me lo quedo.", "Un gusano le dice a otro: Oye, ¿te apetece dar una vuelta a la manzana?", "Estaba una pizza llorando en el cementerio. Llega otra pizza y le dice: ¿Era familiar? No, mediana.", "El profesor le pregunta a Jaimito: ¿Cómo suena la M con la A? Ma.Muy bien. Y si le colocas una tilde, ¿cómo suena? Matilde.", "Papá, papá, me ha mordido una serpiente. ¿Cobra? No, me ha mordido gratis.", "¿Qué hace un perro con un taladro? Ta—ladrando.", "Mamá, mamá, qué buena está la paella.Pues repite, hijo, repite.Mamá, mamá, qué buena está la paella.", "Dos ovejas están jugando al fútbol y una de ellas lanza muy lejos el balón y la otra oveja le dice beeeeeee, a lo que la otra oveja responde veeeeeee tú.", "¿Cuál es el animal que es dos veces animal? El gato, porque es gato y araña.", "¿Cuál es el santo de todas las frutas? La San—día", "¿Cuál es el colmo de un carnicero? Tener una hija chuleta.", "¿En qué se parecen un elefante y una pastilla para dormir? En que el elefante es un paquidermo y la pastilla es paquiduermas.", "Le dice Jaimito a su maestra: Profe, ¿usted me castigaría por algo que yo no he hecho? Claro que no Jaimito. Pues menos mal, porque no he hecho los deberes.", "¿Cómo se dice perro en inglés? Qué fácil, se dice dog. ¿Y cómo se dice veterinario? Pues… dog—tor.", "Van dos vascos por un polígono industrial y ven una empresa que pone: Aceros inoxidables y le dice uno al otro: Eh, Patxi, ¿nos hacemos?", "¿Cuál es el baile favorito del tomate? ¡La salsa!", "Jaimito, si en esta mano tengo ocho naranjas y en esta otra seis naranjas. ¿Qué tengo? Unas manos enormes, maestra.","Dos amigos van por la calle y uno le pregunta al otro: ¿Qué hora es? Son las doce. Ufff, qué tarde. Pues haberme preguntado antes.", "¿Qué le dice un pez a otro? ¡Nada!", "¿Cuál es el colmo de un futbolista? ¡Que le hagan la pelota!", "¿Tienen libros sobre el cansancio? Sí, ¡pero están todos agotados!", "¿Cómo se dice pañuelo en japonés? Sakamoko.", "Un hombre entra en un bar de pinchos y dice: ¡Aaaaaay!.", "Soy un tipo saludable. Ah. ¿te gusta comer sano y hacer deporte? No, la gente me saluda.", "¿Hacía cuánto tiempo que usted no robaba? 5 años señor comisario. Eso está muy bien, ¿y dónde estuvo todos estos 5 años? En la cárcel.", "Mi coronel, hemos perdido la batalla.¡Pues buscadla inmediatamente!", "¿Qué hace un piojo en la cabeza de un calvo? ¡Patinaje sobre hielo!", "Hola guapa, ¿cómo te llamas? Maria de Los Angeles, ¿y tú? Iñaki, de San Sebastián.", "Disculpe, ¿tiene trajes de camuflaje? Sí que los tenía, pero no sé donde, ¡llevo un mes buscándolos!", "Doctor, ¿qué puedo hacer para que me hijo no se haga pis en la cama? Eso tiene fácil solución. Qué duerma en el baño.", "¿Tienen pastillas para el cansancio?Están todas agotadas", "Mamá, ¿me haces un bocadillo de jamón por favor? ¿York? Sí, turk.", "Jaimito, ¿qué planeta va después de Marte? Miércole, señorita.", "¿Qué le dice un árbol a otro? ¡Qué pasa, tronco!", "¿Por qué la escoba es feliz todos los días? Porque siempre ba-rriendo.", "Había una vez un niño tan, tan, tan despistado que... ¡da igual, me he olvidado del chiste!", "Camarero, ese filete tiene muchos nervios. Normal, es la primera vez que se lo comen.", "¿Qué le dice una iguana a su hermana gemela? Somos iguanitas.", "Papá, ¿qué se siente al tener un hijo tan guapo? No sé hijo, pregúntale a tu abuelo.", "Doctor ¡tengo paperas! Pues tome estos 2 euros y ya tienes pa platanos.", "Jaimito, ¿que es la telepatía? Es un aparato de televisión para la hermana de mi mamá.", "¿Por qué está deprimido el libro de matemáticas? Porque tiene muchos problemas.", "¿Cuál es la montaña más limpia? El volcán, porque echa ceniza y después… lava.", "¿Por qué las cigüeñas encogen una pata para dormir? Porque si encogen las dos se caen.", "¿Por qué el maestro de música necesita una escalera? Para alcanzar las notas altas.", "¿Por qué el televisor cruzó la carretera? Porque quería ser pantalla plana.", "¿Cuál es el colmo de las capitales? Estocolmo.", "¿Qué le dijo el cero al ocho? Me gusta tu cinturón."]

dado = ['1', '2', '3', '4', '5']

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
        bot.reply_to(message, "Estos son los comandos disponibles: */añadirme* Añade al usuario a la base de datos de jm (La base de datos es solo para averiguar como funciona etc.), */roll* Este comando lanzara un dado dando un numero aleatorio del 1 al 5, */chistes*, */8ball PREGUNTA*")

@bot.message_handler(commands=["roll", "dado"])
def cmd_dado(message):
        bot.reply_to(message, f"El numero que ha salido es: {random.choice(dado)}")

@bot.message_handler(commands=["chistes"])
def cmd_chistes(message):
        bot.reply_to(message, f"{random.choice(chistes)}")

@bot.message_handler(commands=["8ball", "bola8"])
def cmd_chistes(message):
        bot.reply_to(message, f"{random.choice(respuesta)}")

@bot.message_handler(commands=["stickers"])
def cmd_chistes(message):
        bot.reply_to(message, f"YOU URL")

if __name__=='__main__':
    print('Bot on')
    bot.infinity_polling()
    print("patata")
