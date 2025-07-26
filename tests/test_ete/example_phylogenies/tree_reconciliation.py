from eGPS4Py import Tree, PhyloTree

# Loads a gene tree and its corresponding species tree. Note that
# species names in sptree are the 3 firs letters of leaf nodes in
# genetree.
gene_tree_nw = '((Dme_001,Dme_002),(((Cfa_001,Mms_001),((Hsa_001,Ptr_001),Mmu_001)),(Ptr_002,(Hsa_002,Mmu_002))));'
species_tree_nw = "((((Hsa, Ptr), Mmu), (Mms, Cfa)), Dme);"
genetree = PhyloTree(gene_tree_nw)
sptree = PhyloTree(species_tree_nw)
print(genetree)
#                    /-Dme_001
#          /--------|
#         |          \-Dme_002
#         |
#         |                              /-Cfa_001
#         |                    /--------|
#---------|                   |          \-Mms_001
#         |          /--------|
#         |         |         |                    /-Hsa_001
#         |         |         |          /--------|
#         |         |          \--------|          \-Ptr_001
#          \--------|                   |
#                   |                    \-Mmu_001
#                   |
#                   |          /-Ptr_002
#                    \--------|
#                             |          /-Hsa_002
#                              \--------|
#                                        \-Mmu_002
#
# Let's reconcile our genetree with the species tree
recon_tree, events = genetree.reconcile(sptree)
# a new "reconcilied tree" is returned. As well as the list of
# inferred events.
print("Orthology and Paralogy relationships:")
for ev in events:
    if ev.etype == "S":
        print('ORTHOLOGY RELATIONSHIP:', ','.join(ev.inparalogs), "<====>", ','.join(ev.orthologs))
    elif ev.etype == "D":
        print ('PARALOGY RELATIONSHIP:', ','.join(ev.inparalogs), "<====>", ','.join(ev.outparalogs))
    else:
        print("Other types: ",ev.etype, "\t", ','.join(ev.inparalogs), "<====>", ','.join(ev.outparalogs))
# And we can explore the resulting reconciled tree
print(recon_tree)
# You will notice how the reconciled tree is the same as the gene
# tree with some added branches. They are inferred gene losses.
#
#
#                    /-Dme_001
#          /--------|
#         |          \-Dme_002
#         |
#         |                              /-Cfa_001
#         |                    /--------|
#         |                   |          \-Mms_001
#---------|          /--------|
#         |         |         |                    /-Hsa_001
#         |         |         |          /--------|
#         |         |          \--------|          \-Ptr_001
#         |         |                   |
#         |         |                    \-Mmu_001
#          \--------|
#                   |                    /-Mms
#                   |          /--------|
#                   |         |          \-Cfa
#                   |         |
#                   |         |                              /-Hsa
#                    \--------|                    /--------|
#                             |          /--------|          \-Ptr_002
#                             |         |         |
#                             |         |          \-Mmu
#                              \--------|
#                                       |                    /-Ptr
#                                       |          /--------|
#                                        \--------|          \-Hsa_002
#                                                 |
#                                                  \-Mmu_002
#
# And we can visualize the trees using the default phylogeny
# visualization layout
genetree.show()

print(recon_tree.get_ascii(attributes=[]))

print("-" * 60)
for n in recon_tree.traverse():
    # 打印节点名称
    print(n.name, end="\t")

    # 打印该节点的所有 feature 键值对
    for fname in n.features:          # 这里只是键列表
        fvalue = getattr(n, fname)    # 取出实际的值
        print(f"{fname}={fvalue}", end="\t")

    print()   # 换行