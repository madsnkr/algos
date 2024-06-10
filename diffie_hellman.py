# 1. Agree on public parameters. p = 'prime number', g = 'base'
params = {"p": 7, "g": 5}

# lowercase = priv, uppercase = pub
alice = {"a": 0, "A": 0, "s": 0}
bob = {"b": 0, "B": 0, "s": 0}

# 2. Each party generates a random private key, and a public key
# that's derived from the private key + public parameters

alice["a"] = 120356
alice["A"] = (params["g"] ** alice["a"]) % params["p"]

bob["b"] = 52129
bob["B"] = (params["g"] ** bob["b"]) % params["p"]

# 3. Each party exchange the public keys
alice["B"] = bob["B"]
bob["A"] = alice["A"]

# 4. Computation of shared secret
alice["s"] = (alice["B"] ** alice["a"]) % params["p"]
bob["s"] = (bob["A"] ** bob["b"]) % params["p"]

print(f"Alice's secret: {alice['s']}\nBob's secret: {bob['s']}")
