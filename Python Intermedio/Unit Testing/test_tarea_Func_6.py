from Tarea_Func_6 import organize_from_a_to_z

def test_organize_from_a_to_z_with_100_words():
    #Arrange
    words_to_organize = "river-haven-graze-pluck-pixel-onyx-glyph-yodel-indie-orbit-vivid-kneel-unity-valor-globe-spark-thorn-karma-yacht-frost-jazz" \
    "-solar-fable-coral-apple-flame-epoch-mirth-input-hatch-urban-dunes-maple-crisp-metro-ocean-tiger-ridge-quirk-olive-flint-delta-waltz-twist-irony-" \
    "blaze-kiosk-vibes-cedar-whirl-zebra-radar-latch-magic-stone-pearl-zippy-zesty-yield-swift-lance-ivory-bloom-acorn-ember-quest-nerve-jungle-brave-" \
    "hulk-amber-draft-realm-dream-joker-knack-umbra-lemon-ether-prism-noble-jewel-queen-bridge-xerox-xeric-nifty-xenon-water-venom-lunar-titan-nexus-" \
    "ultra-eagle-quill-arrow-cloud-honey-grace"
    #Act
    organize_from_a_to_z(words_to_organize)
    #Assert
    assert "blaze-hulk-ultra-river-acorn-amber-apple-arrow-bloom-brave-bridge-cedar-cloud-coral-crisp-delta-draft-dream-dunes-eagle-ember-epoch-ether-fable-flame-flint-frost-globe-glyph-grace-graze-hatch-haven-honey-indie-input-irony-ivory-jazz-jewel-joker-jungle-karma-kiosk-knack-kneel-lance-latch-lemon-lunar-magic-maple-metro-mirth-nerve-nexus-nifty-noble-ocean-olive-onyx-orbit-pearl-pixel-pluck-prism-queen-quest-quill-quirk-radar-realm-ridge-solar-spark-stone-swift-thorn-tiger-titan-twist-umbra-unity-urban-valor-venom-vibes-vivid-waltz-water-whirl-xenon-xeric-xerox-yacht-yield-yodel-zebra-zesty-zippy"


def test_organize_from_a_to_z_with_upper_case():
    #Arrange
    words_to_organize = "Zebra-apple-Mango-banana"
    #Act
    organize_from_a_to_z(words_to_organize)
    #Assert
    assert "apple-banana-Mango-Zebra"
    

def test_organize_from_a_to_z_already_sorted():
    #Arrange
    words_to_organize = "apple-banana-cherry-delta-echo"
    #Act
    organize_from_a_to_z(words_to_organize)
    #Assert
    assert "apple-banana-cherry-delta-echo"

