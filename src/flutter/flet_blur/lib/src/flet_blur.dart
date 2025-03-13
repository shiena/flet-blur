import 'dart:async';

import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_acrylic/flutter_acrylic.dart';

class BlurControl extends StatelessWidget {
  final Control? parent;
  final Control control;
  final FletControlBackend backend;

  const BlurControl({
    super.key,
    required this.parent,
    required this.control,
    required this.backend,
  });

  WindowEffect toWindowEffect(String effectName) {
    debugPrint("toWindowEffect($effectName)");
    var lowerName = effectName.toLowerCase();
    var effect = WindowEffect.values.firstWhere(
      (e) => e.name.toLowerCase() == lowerName,
      orElse: () => WindowEffect.disabled,
    );
    return effect;
  }

  @override
  Widget build(BuildContext context) {
    () async {
      backend.subscribeMethods(control.id, (methodName, args) async {
        switch (methodName) {
          case "setWindowEffect":
            var effect = toWindowEffect(args["effect"] ?? "");
            var bgColor =
                control.attrColor("blurBgcolor", context) ?? Colors.transparent;
            var dark = (args["dark"] ?? "true").toLowerCase() == "true";
            await Window.setEffect(effect: effect, color: bgColor, dark: dark);
            break;
        }
        return null;
      });
    }();
    return const SizedBox.shrink();
  }
}
