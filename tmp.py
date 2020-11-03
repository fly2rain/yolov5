print("hello world")

# with open(log_dir / 'hyp.yaml', 'w') as f:
#     yaml.dump(hyp, f, sort_keys=False)

if __name__ == "__main__":
    ratio_str = "0.7  0.1  0.2"
    ratio = [float(x.strip()) for x in ratio_str.split()]
    print(ratio_str)
    print(ratio)

    print(sum(ratio))
    print([x/sum(ratio) for x in ratio])